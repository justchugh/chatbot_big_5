
import discord
from discord.ext import commands
import random
from datetime import datetime

bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix, case_insensitive=True)

command_count = 0

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running.")
    await bot.change_presence(activity=discord.Game(name=f"{bot.command_prefix}help_commands"))

@bot.command(name="ping")
async def ping(ctx):
    global command_count
    await ctx.send(f"Pong! Latency is {round(bot.latency * 1000)}ms")
    command_count += 1

@bot.command(name="time")
async def time(ctx):
    global command_count
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Current time: {current_time}")
    command_count += 1

@bot.command(name="command_usage")
async def command_usage(ctx):
    global command_count
    await ctx.send(f"Commands used: {command_count}")
    command_count += 1

@bot.command(name="number_game")
async def number_game(ctx):
    global command_count
    secret_number = random.randint(1, 10)
    await ctx.send("Guess a number between 1 and 10")

    def validate_guess(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    try:
        guess = await bot.wait_for("message", check=validate_guess, timeout=15.0)
        if int(guess.content) == secret_number:
            await ctx.send("Correct guess!")
        else:
            await ctx.send(f"Wrong guess! The number was {secret_number}")
    except asyncio.TimeoutError:
        await ctx.send("Time's up! You took too long.")

    command_count += 1

@bot.command(name="help_commands")
async def help_commands(ctx):
    global command_count
    help_msg = (
        "!ping - Check latency
"
        "!time - Get the current time
"
        "!command_usage - Command usage count
"
        "!number_game - Play a number guessing game
"
    )
    await ctx.send(help_msg)
    command_count += 1

bot.run('YOUR_BOT_TOKEN')
