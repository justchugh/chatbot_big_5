import discord
from discord.ext import commands
from datetime import datetime
import random
import os

# Load the bot token from an environment variable for security
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

prefix = "!!"
client = commands.Bot(command_prefix=prefix, case_insensitive=True)

times_used = 0

@client.event
async def on_ready():
    print(f"I am ready to go - {client.user.name}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{client.command_prefix}python_help. This bot is made by drakeerv."))

@client.command(name="ping")
async def _ping(ctx):
    global times_used
    await ctx.send(f"Ping: {client.latency}")
    times_used += 1

@client.command(name="time")
async def _time(ctx):
    global times_used
    now = datetime.now()

    am_pm = "AM" if now.strftime("%H") <= "12" else "PM"
    current_time = now.strftime("%m/%d/%Y, %I:%M")

    await ctx.send("Current Time: " + current_time + ' ' + am_pm)
    times_used += 1

@client.command(name="times_used")
async def _used(ctx):
    global times_used
    await ctx.send(f"Times used since last reboot: {times_used}")
    times_used += 1

@client.command(name="python_help")
async def _python_help(ctx):
    global times_used
    msg = '\r\n'.join(["!!help: returns all of the commands and what they do.",
                       "!!time: returns the current time.",
                       "!!ping: returns the ping to the server."])
    await ctx.send(msg)
    times_used += 1

@client.command()
async def command(ctx):
    computer = random.randint(1, 10)
    await ctx.send('Guess my number')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit() and 1 <= int(msg.content) <= 10

    msg = await client.wait_for("message", check=check)

    if int(msg.content) == computer:
        await ctx.send("Correct")
    else:
        await ctx.send(f"Nope, it was {computer}")

# Run the bot with the token from the environment variable
client.run(TOKEN)
