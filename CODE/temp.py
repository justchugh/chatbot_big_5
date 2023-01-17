
import discord
from discord.ext import commands
import random
from datetime import datetime

bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix, case_insensitive=True)

cmd_count = 0

@bot.event
async def on_ready():
    print(f"{bot.user.name} is running.")
    await bot.change_presence(activity=discord.Game(name=f"{bot.command_prefix}help_commands"))

@bot.command(name="ping")
async def ping(ctx):
    global cmd_count
    await ctx.send(f"Pong! Latency is {round(bot.latency * 1000)}ms")
    cmd_count += 1

@bot.command(name="time")
async def time(ctx):
    global cmd_count
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Current time: {now}")
    cmd_count += 1

@bot.command(name="command_count")
async def command_count(ctx):
    global cmd_count
    await ctx.send(f"Commands used: {cmd_count}")
    cmd_count += 1

@bot.command(name="guess_the_number")
async def guess_the_number(ctx):
    global cmd_count
    number = random.randint(1, 10)
    await ctx.send("Guess a number between 1 and 10")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    try:
        guess = await bot.wait_for("message", check=check, timeout=15.0)
        if int(guess.content) == number:
            await ctx.send("Correct guess!")
        else:
            await ctx.send(f"Nope! It was {number}")
    except asyncio.TimeoutError:
        await ctx.send("You took too long.")

    cmd_count += 1

@bot.command(name="help_commands")
async def help_commands(ctx):
    global cmd_count
    help_text = (
        "!ping - Bot's latency
"
        "!time - Current time
"
        "!command_count - Number of commands used
"
        "!guess_the_number - Number guessing game
"
    )
    await ctx.send(help_text)
    cmd_count += 1

bot.run('YOUR_BOT_TOKEN')
