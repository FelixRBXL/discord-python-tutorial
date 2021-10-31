import discord
from discord.ext import *
import asyncio

client = commands.Bot(command_prefix=".")
client.remove_command('help')

@client.event
async def on_ready():
    print("{} is online!".format(client.user.name))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Felix. Community Server"))
        await asyncio.sleep(5) # Wenn der Status alle 10 Sekunden ändern soll, änder die '5' zur '10' oder in die Zahl, die du willst.
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{members} Mitglieder."))

#####################################################################################################

@client.command(name="hello")
async def hello(ctx, member:discord.Member=None):
    if member == None:
        member = ctx.author
    await ctx.send(f"Hallo {member.mention}!")

@client.command(name="embed")
async def embed(ctx):
    embed=discord.Embed(title="Embed Title", description="Embed Description", color=0xff0000)
    embed.add_field(name="Field Name", value="Field Value", inline=False) # Wenn du willst, dass das Feld in der Reihe seinen soll, stelle das False auf True
    embed.set_thumbnail(url="") # Setze in die Klammern die URL eines Bildes
    embed.set_image(url="") # Setze in die Klammern die URL eines Bildes
    embed.set_footer(text="Embed Footer")
    await ctx.send(embed=embed)

client.run("") # Füge hier deinen TOKEN ein. Wie du den TOKEN suchst, lese '6. Wie kriege ich den Token?' in der ReadMe-Datei.
