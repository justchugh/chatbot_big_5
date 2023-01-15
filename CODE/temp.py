
import discord
from discord.ext import commands
import random

prefix = "!"
client = commands.Bot(command_prefix=prefix, case_insensitive=True)

usage_counter = 0

@client.event
async def on_ready():
    print(f"Bot is ready - {client.user.name}")
    await client.change_presence(activity=discord.Game(name=f"{client.command_prefix}help"))

@client.command(name="ping")
async def ping(ctx):
    global usage_counter
    await ctx.send(f"Pong! Latency: {round(client.latency * 1000)}ms")
    usage_counter += 1

@client.command(name="current_time")
async def current_time(ctx):
    global usage_counter
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Current time: {formatted_time}")
    usage_counter += 1

@client.command(name="usage_stats")
async def usage_stats(ctx):
    global usage_counter
    await ctx.send(f"Commands used: {usage_counter}")
    usage_counter += 1

@client.command(name="number_guess")
async def number_guess(ctx):
    global usage_counter
    target_number = random.randint(1, 10)
    await ctx.send("Guess a number between 1 and 10")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    try:
        guess = await client.wait_for("message", check=check, timeout=15.0)
        if int(guess.content) == target_number:
            await ctx.send("You guessed it!")
        else:
            await ctx.send(f"Wrong! The number was {target_number}")
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to respond.")

    usage_counter += 1

@client.command(name="help")
async def help_command(ctx):
    global usage_counter
    help_message = (
        "!ping - Check the bot's latency
"
        "!current_time - Get the current time
"
        "!usage_stats - See how many commands have been used
"
        "!number_guess - Play a number guessing game
"
    )
    await ctx.send(help_message)
    usage_counter += 1

client.run('YOUR_BOT_TOKEN')
