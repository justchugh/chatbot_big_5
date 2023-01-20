
import discord
from discord.ext import commands
import random

prefix = "!"
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

usage_count = 0

@bot.event
async def on_ready():
    print(f"Bot is online - {bot.user.name}")
    await bot.change_presence(activity=discord.Game(name=f"{bot.command_prefix}commands"))

@bot.command(name="ping")
async def ping(ctx):
    global usage_count
    await ctx.send(f"Ping! Latency is {round(bot.latency * 1000)}ms")
    usage_count += 1

@bot.command(name="current_time")
async def current_time(ctx):
    global usage_count
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Current time: {current_time}")
    usage_count += 1

@bot.command(name="usage")
async def usage(ctx):
    global usage_count
    await ctx.send(f"Total commands used: {usage_count}")
    usage_count += 1

@bot.command(name="guess_number")
async def guess_number(ctx):
    global usage_count
    number = random.randint(1, 10)
    await ctx.send("Guess a number between 1 and 10")

    def is_correct(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    try:
        guess = await bot.wait_for("message", check=is_correct, timeout=15.0)
        if int(guess.content) == number:
            await ctx.send("Correct!")
        else:
            await ctx.send(f"Incorrect! The number was {number}")
    except asyncio.TimeoutError:
        await ctx.send("You took too long to guess.")

    usage_count += 1

@bot.command(name="commands")
async def commands(ctx):
    global usage_count
    commands_list = (
        "!ping - Check the bot's latency
"
        "!current_time - Get the current time
"
        "!usage - See command usage count
"
        "!guess_number - Play a guessing game
"
    )
    await ctx.send(commands_list)
    usage_count += 1

bot.run('YOUR_BOT_TOKEN')
