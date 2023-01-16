
import discord
from discord.ext import commands
import random
from datetime import datetime

bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix, case_insensitive=True)

cmd_usage = 0

@bot.event
async def on_ready():
    print(f"{bot.user.name} is up and running.")
    await bot.change_presence(activity=discord.Game(name=f"{bot.command_prefix}assist"))

@bot.command(name="ping")
async def ping(ctx):
    global cmd_usage
    await ctx.send(f"Pong! Latency: {round(bot.latency * 1000)}ms")
    cmd_usage += 1

@bot.command(name="time")
async def time(ctx):
    global cmd_usage
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Time now: {now}")
    cmd_usage += 1

@bot.command(name="usage")
async def usage(ctx):
    global cmd_usage
    await ctx.send(f"Command count: {cmd_usage}")
    cmd_usage += 1

@bot.command(name="guess")
async def guess(ctx):
    global cmd_usage
    number = random.randint(1, 10)
    await ctx.send("Guess a number between 1 to 10")

    def validate(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    try:
        guess = await bot.wait_for("message", check=validate, timeout=15.0)
        if int(guess.content) == number:
            await ctx.send("Correct guess!")
        else:
            await ctx.send(f"Wrong guess! It was {number}")
    except asyncio.TimeoutError:
        await ctx.send("You took too long.")

    cmd_usage += 1

@bot.command(name="assist")
async def assist(ctx):
    global cmd_usage
    help_text = (
        "!ping - Latency check
"
        "!time - Current time
"
        "!usage - Command usage count
"
        "!guess - Number guessing game
"
    )
    await ctx.send(help_text)
    cmd_usage += 1

bot.run('YOUR_BOT_TOKEN')
