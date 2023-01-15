
import discord
from discord.ext import commands
import random

bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix, case_insensitive=True)

command_usage = 0

@client.event
async def on_ready():
    print(f"{client.user.name} is ready.")
    await client.change_presence(activity=discord.Game(name=f"{client.command_prefix}help"))

@client.command(name="ping")
async def ping(ctx):
    global command_usage
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
    command_usage += 1

@client.command(name="current_time")
async def current_time(ctx):
    global command_usage
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Current time: {now}")
    command_usage += 1

@client.command(name="usage_count")
async def usage_count(ctx):
    global command_usage
    await ctx.send(f"Commands used: {command_usage}")
    command_usage += 1

@client.command(name="number_guess")
async def number_guess(ctx):
    global command_usage
    secret_number = random.randint(1, 10)
    await ctx.send("Guess a number between 1 and 10")

    def check_guess(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    try:
        guess = await client.wait_for("message", check=check_guess, timeout=15.0)
        if int(guess.content) == secret_number:
            await ctx.send("That's right!")
        else:
            await ctx.send(f"Nope! The number was {secret_number}")
    except asyncio.TimeoutError:
        await ctx.send("You didn't respond in time.")

    command_usage += 1

@client.command(name="help")
async def help_command(ctx):
    global command_usage
    help_text = (
        "!ping - Bot's latency
"
        "!current_time - Current time
"
        "!usage_count - Number of commands used
"
        "!number_guess - Guess the number game
"
    )
    await ctx.send(help_text)
    command_usage += 1

client.run('YOUR_BOT_TOKEN')
