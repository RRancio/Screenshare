# <=============== Design ====================>

# <=============== Design imports ====================>
from colorama import init, Fore, Back, Style
from tqdm import tqdm, trange
from time import sleep
import os
# <=============== Design imports End ====================>
v = "3.4.0"
print(
    f"""
{Fore.LIGHTCYAN_EX}

                                         

                                                         
                                      //   ) )                                             
                                     ((         ___      __      ___      ___   __     
                                      \\     //   ) ) //  ) ) //___) ) //___) )//  ) )  
                                       ) ) //       //      //       //       //   / /   
                                ((___ / / ((____   //      ((____   ((____   //   / /    
                                                          
                                                    //   ) )                                   
                                                    ((       / __      ___      __      ___    
                                                    \\     //   ) )  //   ) ) //  ) ) //___) ) 
                                                      ) ) //    / / //   / / //      //        
                                               ((___ / / //    / / ((___( ( //      ((____     


{Fore.LIGHTCYAN_EX}
                                                        
                                                        Version: {v}

                                        {Fore.WHITE}                   Loading...


""")

# <=============== End of Design ====================>


# <===========================Imports==============================>

import discord
import sys
import traceback
import datetime
import re
import json
import asyncio
import googletrans
import random
import urllib
import datetime as dt
import requests as req
import requests as niggaip
import requests as nonniggaip
from discord import Embed
from googletrans import Translator
from discord.ext import commands
from discord.ext import tasks
from discord import Activity, ActivityType
from discord import Permissions
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import command, cooldown, MissingRequiredArgument, CommandNotFound, BadArgument, CommandOnCooldown

# <===========================Imports end==============================>


# <=========================== Bot propieties ==============================>
client =  discord.Client()
bot = commands.Bot(command_prefix='!', case_insensitive=True)
logchannel = bot.get_channel(811988319733809162)
bot.remove_command("help")
help_command = commands.MinimalHelpCommand()
owners = [811771656368291840, 716700259572777022]
# <=========================== Bot propieties ==============================>

# <=========================== On Ready ==============================>
@tasks.loop(seconds=5.0)
async def my_background_task():
    await bot.change_presence(activity=discord.Streaming(name="🔎 Prefix: !", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    await bot.change_presence(activity=discord.Streaming(name="🔎 Version 3.4.0", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    my_background_task.start()
    os.system("clear")
    os.system("cls")
    print(f"""               
    {Fore.LIGHTBLUE_EX}           
                         
                                              (%%%%%%%%%%%                                 
                                           %%%             %%                              
                                         ,%%                 %%                            
                                        .%.                   %%                           
                                        %%                     %                           
                                        %%  %%                (%                           
                                         %% %%%               %#                           
                                          %%% %%%%%%%%      %%%                            
                                             %%%        .%%% %%%%%%%%                      
                                                  (%%%.       %%%%%%%%%%                   
                                                                 %%%%%%%%%                 
                                                                     %%%%       

                                       Guilds: {len(bot.guilds)} Version: 3.4.0        
                                                      

          
                                                                 
""")
# <=========================== On Ready ==============================>

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        ss = discord.Embed(timestamp=ctx.message.created_at, description ="This command was not found", color=0x3498db)
        ss.set_author(name=f'Wrong command', icon_url='https://cdn.discordapp.com/attachments/874385566400127097/896019949401829407/Frame_8_1.png')
        ss.set_footer(text=f"Command error | ")
        await ctx.send(embed=ss)

@bot.event
async def on_guild_join(ctx):
    logchannel = bot.get_channel(872829031236665354)
    await logchannel.send("Hi, i got invited on a new discord!")
    await logchannel.send(f"Total guilds:{len(bot.guilds)}")

# <=========================== Bot propieties End ==============================>

# <=========================== Commands ==============================>

#                             <Moderation>
@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member=None, *, reason="No reason"):
    logchannel = bot.get_channel(872829031236665354)
    if user == None:

        # < =============== Animation ==================================================================================================== >
        juice=discord.Embed(color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice5=discord.Embed(title="⚠️ Error, are you trying to ban anyone?", description="Usage: !ban @user (reason)", color=discord.Colour.gold())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice5)
        return
    if user == ctx.message.author:
        juice=discord.Embed(color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice10=discord.Embed(title="⚠️ Error, You cant ban yourself", color=discord.Color.red())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice10)
        return
    else:
        juice=discord.Embed(color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice15=discord.Embed(title="✓", color=discord.Color.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await user.ban(reason=reason)
        await msg.delete()
        # < =============== Animation ==================================================================================================== >

        juice=discord.Embed(timestamp=ctx.message.created_at, title=f"Ban", color=0x3498db)
        juice.add_field(name="User banned", value=user.name, inline=False)
        juice.add_field(name="Reason", value=reason, inline=False)
        juice.add_field(name="ID:", value=user.id, inline=False)
        juice.add_field(name="Executed by", value=ctx.message.author, inline=False)
        juice.set_footer(text="Ban | ")
        await ctx.send(embed=juice)

        # < ======================== LOG ==================================================>
        await msg.edit(embed=juice14)
        juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
        juice2.add_field(name=f"Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
        juice2.add_field(name=f"Command", value=f"!ban", inline=False)
        juice2.add_field(name=f"User banned", value=user.name, inline=False)
        juice2.add_field(name=f"Reason", value=reason)
        juice2.add_field(name=f"User ID", value=ctx.message.author.id, inline=False)
        juice2.add_field(name=f"Guild", value=ctx.guild.name, inline=False)
        juice2.add_field(name=f"Guild ID", value=ctx.guild.id, inline=False)
        juice2.set_footer(text="logs | Ban")
        await logchannel.send(embed=juice2)
        # < ======================== LOG ==================================================>

@bot.command(aliases=["ub"])
async def unban(ctx, *, member):
     logchannel = bot.get_channel(872829031236665354)
     banned_users = await ctx.guild.bans()
     member_name, member_discriminator = member.split ("#")
     
     for ban_entry in banned_users:
         user = ban_entry.user
         if (user.name, user.discriminator) == (member_name, member_discriminator):

             # < =============== Animation ==================================================================================================== >
             juice=discord.Embed(color=0x3498db)
             juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
             juice15=discord.Embed(title="✓", color=discord.Color.green())
             msg = await ctx.send(embed=juice)
             await asyncio.sleep(1)
             await msg.edit(embed=juice15)
             await ctx.guild.unban(user)
             await msg.delete()

             # < =============== Animation ==================================================================================================== >
             juice2=discord.Embed(timestamp=ctx.message.created_at, title="Unban", color=0x3498db)
             juice2.add_field(name="user unbanned", value=f"{member_name}#{member_discriminator}", inline=False)
             juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
             juice2.add_field(name="Executor", value=ctx.message.author, inline=False)
             juice2.set_footer(text="unban | ")
             await ctx.send(embed=juice2)

             # < ======================== LOG ==================================================>
             juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
             juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
             juice2.add_field(name="Command", value=f"!unban", inline=False)
             juice2.add_field(name="User unbaned", value=f"{member_name}#{member_discriminator}", inline=False)
             juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
             juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
             juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
             juice2.set_footer(text="logs | unban")
             await logchannel.send(embed=juice2)
             # < ======================== LOG ==================================================>

@bot.command(name="kick")
@has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member=None, *, reason="No reason provided"):
    logchannel = bot.get_channel(872829031236665354)
    if user == None:

        # < =============== Animation ==================================================================================================== >
        juice=discord.Embed(color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice15=discord.Embed(title="⚠️ Error, are you trying to kick anyone?", color=discord.Colour.gold())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice15)
        return
        # < =============== Animation ==================================================================================================== >

    else:

        # < =============== Animation ==================================================================================================== >
        juice=discord.Embed(color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice15=discord.Embed(title="✓", color=discord.Color.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice15)
        await asyncio.sleep(0.50)
        await msg.delete()
        # < =============== Animation ==================================================================================================== >

        await user.kick(reason=reason)
        juice=discord.Embed(timestamp=ctx.message.created_at, title=f"Kick", color=0x3498db)
        juice.add_field(name="User kicked", value=user.name, inline=False)
        juice.add_field(name="Reason", value=reason, inline=False)
        juice.add_field(name="ID:", value=user.id, inline=False)
        juice.add_field(name="Executed by", value=ctx.message.author, inline=False)
        juice.set_footer(text="Kick | ")
        await ctx.send(embed=juice)

        # < ======================== LOG ==================================================>
        juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
        juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
        juice2.add_field(name="Command", value=f"!kick", inline=False)
        juice2.add_field(name="User kicked", value=user.name, inline=False)
        juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
        juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
        juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
        juice2.set_footer(text="logs | unban")
        await logchannel.send(embed=juice2)
        # < ======================== LOG ==================================================>

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, user: discord.Member, *, reason="No reason provided"):
    guild = ctx.guild
    if user == ctx.message.author:

        # < =============== Animation ==================================================================================================== >
        juice=discord.Embed(color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice26=discord.Embed(title="⚠️ Error, are you trying to mute yourself?", color=discord.Colour.gold())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice26)
        return
        # < =============== Animation ==================================================================================================== >

    mutedRole = discord.utils.get(guild.roles, name="Muted")


    if not mutedRole:

        # < =============== Animation ==================================================================================================== >
        mutedRole = await guild.create_role(name="Muted")
        juice=discord.Embed(description="Mute role was not found.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice2=discord.Embed(description="Creating one.", color=0x3498db)
        juice2.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice3=discord.Embed(description="Defining permissions.", color=0x3498db)
        juice3.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice4=discord.Embed(description="Editing channels..", color=0x3498db)
        juice4.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice5=discord.Embed(title="✓ Role was created successfully", description="This action would take some seconds", color=discord.Color.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(0.30)
        await msg.edit(embed=juice2)
        await asyncio.sleep(0.30)
        await msg.edit(embed=juice3)
        await asyncio.sleep(0.30)
        await msg.edit(embed=juice4)
        await asyncio.sleep(0.30)
        await msg.edit(embed=juice5)
        # < =============== Animation ==================================================================================================== >

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    juice4=discord.Embed(color=0x3498db)
    juice4.set_author(name="Muting user.", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    juicemsg = await ctx.send(embed=juice4)
    await asyncio.sleep(1)
    await juicemsg.delete()
    juice222=discord.Embed(timestamp=ctx.message.created_at, title=f"Mute", color=0x3498db)
    juice222.add_field(name="User muted", value=user.name, inline=False)
    juice222.add_field(name="Reason", value=reason, inline=False)
    juice222.add_field(name="User ID", value=user.id, inline=False)
    juice222.add_field(name="Author", value=ctx.message.author, inline=False)
    juice222.set_footer(text="Mute |")
    await ctx.send(embed=juice222)
    await user.add_roles(mutedRole, reason=reason)
      
    # < ======================== LOG ==================================================>
    logchannel = bot.get_channel(872829031236665354)
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!mute", inline=False)
    juice2.add_field(name="User muted", value=user, inline=False)
    juice2.add_field(name="Reason", value=reason, inline=False)
    juice2.add_field(name="User ID", value=user.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | mute")
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>
    
@bot.command()
@has_permissions(manage_roles=True)
async def unmute(ctx, user : discord.Member, *, unit = None):
    logchannel = bot.get_channel(872829031236665354)
    if user == ctx.message.author:

        # < =============== Animation ==================================================================================================== >
        juice=discord.Embed(description="Trying to unmute.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice5=discord.Embed(title="⚠️ Error, are you trying to unmute yourself?", description="Wait, if you're trying to unmute yourself, how you are muted?", color=discord.Colour.gold())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice5)
        return
        # < =============== Animation ==================================================================================================== >

    if user == None:

        # < =============== Animation ==================================================================================================== >
        juice=discord.Embed(description="Trying to unmute.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice2=discord.Embed(title="⚠️ Error, are you trying to unmute anyone?", description="Usage: !unmute @user", color=discord.Color.red())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice2)
        # < =============== Animation ==================================================================================================== >

    else:
        roleobject = discord.utils.get(ctx.message.guild.roles, name="Muted")

        # < =============== Animation ==================================================================================================== >
        juice=discord.Embed(description="Trying to unmute.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        juice2=discord.Embed(title="✓", color=discord.Color.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=juice2)
        await asyncio.sleep(0.50)
        await msg.delete()
        # < =============== Animation ==================================================================================================== >
        
        await user.remove_roles(roleobject)
        juice3=discord.Embed(title=f"Unmute", color=0x3498db)
        juice3.add_field(name="User unmuted", value=user, inline=False)
        juice3.add_field(name="User ID", value=user.id, inline=False)
        juice3.add_field(name="Author", value=ctx.message.author, inline=False)
        await ctx.send(embed=juice3)

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!unmute", inline=False)
    juice2.add_field(name="User unmuted", value=user, inline=False)
    juice2.add_field(name="User ID", value=user.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | unmute")
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

#                             <Moderation END>

#                                <Utils>


@bot.command()
@has_permissions(administrator=True)
async def slist(ctx):
    logchannel = bot.get_channel(872829031236665354)
    juice=discord.Embed(timestamp=ctx.message.created_at, title="Screenshare Server list", description=f"Total guilds: {len(bot.guilds)} (Probably more guilds than 8 might non be showed for some reason)" , color=0x3498db)
    for guild in bot.guilds:
        juice.add_field(name="Server Name", value=guild.name)
        juice.add_field(name="Members", value=guild.member_count)
        juice.add_field(name="ID", value=guild.id)
        juice.set_footer(text="Server List |")
    await ctx.send(embed=juice)

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!eslist", inline=False)
    juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | eslist")
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

        
        

@bot.command()
@has_permissions(administrator=True)
async def ESlist(ctx):
    logchannel = bot.get_channel(872829031236665354)
    for guild in bot.guilds:
        await ctx.send(f"```Server Name: {guild.name}  Members: {guild.member_count}  ID: {guild.id}```")
    await ctx.send(f"Total guilds: {len(bot.guilds)}")

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!eslist", inline=False)
    juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | eslist")
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

@bot.command(pass_context=True, aliases=["cl"])
@has_permissions(manage_messages=True)
async def clear(ctx, amount=0,):
    logchannel = bot.get_channel(872829031236665354)
    channel = ctx.message.channel
    messages = []
    await ctx.message.delete()
    if amount == 0:
       juice=discord.Embed(description="**Choose a number:** 1-100" , color=0x3498db)
       juice.set_footer(text="Screenshare 🧃")
       await ctx.send(embed=juice)
       await ctx.message.delete() 
       return
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    juice=discord.Embed(title="Clear" , color=0x3498db)
    juice.set_author(name=ctx.author.display_name, url="https://cdn.discordapp.com/attachments/874385566400127097/896019949401829407/Frame_8_1.png", icon_url=ctx.author.avatar_url)
    juice.set_thumbnail(url="https://cdn.discordapp.com/attachments/874385566400127097/896019949401829407/Frame_8_1.png")
    juice.add_field(name="Messages cleared successfully", value=f"Amount: **{amount}**" , inline=False)
    juice.set_footer(text="Clear | ")
    await ctx.send(embed=juice)

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!clear", inline=False)
    juice2.add_field(name="Amount", value=amount, inline=False)
    juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_Juice-botfooter(text="logs | clear")
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

@bot.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, limit=100):
    channel = ctx.channel
    channel_position = channel.position
    channel2 = ctx.message.channel
    messages = await ctx.channel.history(limit=limit).flatten()
   
    with open(f"Nuked_{channel2}_messages.txt", "a+", encoding="utf-8") as f:
        print(f"\nTranscript Saved by - {ctx.author.display_name}.\n\n", file=f)
        for message in messages:
            embed = ""
            if len(message.embeds) != 0:
                embed = message.embeds[0].description
                print(f"{message.author.name} - {embed}", file=f)
            print(f"{message.author.name} - {message.content}", file=f)

    # < =============== Animation ================= >
    er=discord.Embed(title="Channel will be nuked in", color=0x3498db)
    do=discord.Embed(title="3", color=0x3498db)
    ero=discord.Embed(title="2", color=0x3498db)
    to=discord.Embed(title="1", color=discord.Colour.gold())
    to2=discord.Embed(title="🧃", color=discord.Colour.red())
    msg = await ctx.send(embed=er)
    await msg.edit(embed=do)
    await asyncio.sleep(0.30)
    await msg.edit(embed=ero)
    await asyncio.sleep(0.30)
    await msg.edit(embed=to)
    await asyncio.sleep(0.30)
    await msg.edit(embed=to2)
    await asyncio.sleep(0.30)
    await msg.delete()
    # < =============== Animation ================= >

    new_channel = await channel.clone()
    await channel.delete()
    await new_channel.edit(position=channel_position)
    juice=discord.Embed(title="Channel got nuked :)" , color=0x3498db)
    juice.set_image(url="https://cdn.discordapp.com/attachments/791149140817739786/809495958999007282/nuke.gif")
    await new_channel.send(embed=juice)

    
    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!nuke", inline=False)
    juice2.add_field(name="Channel", value=channel, inline=False)
    juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | nuke")
    logchannel = bot.get_channel(872829031236665354)
    history = discord.File(fp=f'Nuked_{channel2}_messages.txt', filename=None)
    await logchannel.send(embed=juice2)
    await logchannel.send(file=history)
    await logchannel.send("```                                       ```")
    # < ======================== LOG ==================================================>
    return


@bot.command()
@commands.has_permissions(manage_channels=True)
async def fnuke(ctx, limit=100):

    channel = ctx.channel
    channel_position = channel.position
    channel2 = ctx.message.channel
    messages = await ctx.channel.history(limit=limit).flatten()
   
    with open(f"Nuked_{channel2}_messages.txt", "a+", encoding="utf-8") as f:
        print(f"\nTranscript Saved by - {ctx.author.display_name}.\n\n", file=f)
        for message in messages:
            embed = ""
            if len(message.embeds) != 0:
                embed = message.embeds[0].description
                print(f"{message.author.name} - {embed}", file=f)
            print(f"{message.author.name} - {message.content}", file=f)

    new_channel = await channel.clone()
    await channel.delete()
    await new_channel.edit(position=channel_position)
    juice=discord.Embed(title="Channel got fast nuked :)" , color=0x3498db)
    juice.set_image(url="https://cdn.discordapp.com/attachments/791149140817739786/809495958999007282/nuke.gif")
    await new_channel.send(embed=juice)

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!fnuke", inline=False)
    juice2.add_field(name="Channel", value=channel, inline=False)
    juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | nuke")
    logchannel = bot.get_channel(872829031236665354)
    history = discord.File(fp=f'Nuked_{channel2}_messages.txt', filename=None)  
    await logchannel.send(embed=juice2)
    await logchannel.send(file=history)
    await logchannel.send("```                                       ```")
    # < ======================== LOG ==================================================>
    return

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    juice=discord.Embed(title="Added role successfully", description=f"Role {role.name} was successfully given to {user.name}", color=0x3498db)
    await ctx.send(embed=juice)

     # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!addrole", inline=False)
    juice2.add_field(name="Also added role", value=role.name)
    juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | addrole")
    logchannel = bot.get_channel(872829031236665354)
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

@bot.command(aliases=["remrole"])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    juice=discord.Embed(title="Removed role successfully", description=f"Role {role.name} was successfully removed from {user.name}", color=0x3498db)
    await ctx.send(embed=juice)
    
    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!addrole", inline=False)
    juice2.add_field(name="Also removed role", value=role.name)
    juice2.add_field(name="User ID", value=ctx.message.author.id, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | remove role")
    logchannel = bot.get_channel(872829031236665354)
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

@bot.command()
async def dns(ctx, *,dns=None):
    logchannel = bot.get_channel(872829031236665354)
    if dns == None:

    	# < =============== Animation ================= >
        juice=discord.Embed(description="Checking DNS.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to2=discord.Embed(title="⚠️ Error, You dont put an DNS", color=discord.Color.gold())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=to2)
        return
        # < =============== Animation ================= >

    # < =============== Animation ================= >
    juice=discord.Embed(description="Checking DNS.", color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    to2=discord.Embed(title="✓", color=discord.Colour.green())
    msg = await ctx.send(embed=juice)
    await asyncio.sleep(1)
    await msg.edit(embed=to2)
    await asyncio.sleep(0.50)
    await msg.delete() 
    # < =============== Animation ================= >

    DNS=req.get("https://api.hackertarget.com/dnslookup/?q=" + dns)
    juice = discord.Embed(timestamp=ctx.message.created_at, color=0x3498db, description="" + str(str(DNS.text).replace("\"", " ").replace("{", " ").replace("}", " ").replace(",", " ").replace("A :", "DNS:").replace("MX :", """Mail exchange:""").replace("NS :", "Server Name:").replace("TXT :", "TXT Registry:").replace("-", " ").replace("verification=", "Verification: ").replace("SOA :", "Server owner name: ")))
    juice.set_author(name=f'DNS Lookup', icon_url='https://cdn.discordapp.com/attachments/812592984506892318/812864353627013120/image_processing20200510-6203-4b3uiw.png')
    juice.set_footer(text=f"Looked up by: {ctx.message.author} |")
    await ctx.channel.send(embed=juice)

@bot.command()
async def ip(ctx, ip=None):
    if ip == None:

        # < =============== Animation ================= >
        juice=discord.Embed(description="Checking IP Address.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to2=discord.Embed(title="⚠️ Error, You dont put an IP Number", color=discord.Color.gold())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=to2)
        return
        # < =============== Animation ================= >
        
    else:
        urls="http://extreme-ip-lookup.com/json/"+ str(ip)
        ipinfo = niggaip.get(urls)#request api
        urls2="https://proxycheck.io/v2/" + str(ip) + "?vpn=1&asn=1"
        ipinfo2 = nonniggaip.get(urls2)#request api

        # < =============== Animation ================= >
        juice=discord.Embed(description="Checking IP Address.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to222=discord.Embed(title="✓", color=discord.Color.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.delete()
        # < =============== Animation ================= > 

        juice = discord.Embed(timestamp=ctx.message.created_at, color=0x3498db)
        juice.set_author(name=f'IP Lookup ', icon_url='https://cdn.discordapp.com/attachments/791149140817739786/811393616144629780/satellite-antenna-emoji-clipart-md.png')
        juice.add_field(name="Type 1", value=str(ipinfo.text).replace("\"", "").replace("{", "").replace("}", "").replace(",", "").replace("businessName :", "").replace("businessWebsite :", "").replace("city :", "City:").replace("continent :", "Continent:").replace("country :", "Country:").replace("countryCode :", "Country Code:").replace("ipName :", "IP Name:").replace("ipType :", "IP Type:").replace("isp :", "ISP:").replace("lat :", "Latitude:").replace("lon :", "Longitude:").replace("org :", "Organization:").replace("query :", "IP:").replace("region :", "Region:").replace("status :", "IP status:").replace("status:failmessage:query is", "Lookup error:"), inline=False)
        juice.add_field(name="Type 2", value=str(ipinfo2.text).replace("\"", "").replace("{", "").replace("}", "").replace(",", "").replace("status: ok", "Status: Valid").replace("asn:", "ASN:").replace("provider:", "Provider:").replace("continent:", "Continent:").replace("country:", "Country:").replace("isocode:", "ISO Code:").replace("region:", "Region:").replace("regioncode:", "Region Code:").replace("city:", "City:").replace("proxy:", "Proxy / VPN:").replace("type:", "Type:"), inline=False)
        juice.set_footer(text=f"Looked up by: {ctx.message.author} | " + str(ip))
        await ctx.send(embed=juice)

@bot.command(name="alts")
async def alts(ctx, player):#, minecraft: str):

    response = requests.get(f"https://api.echo.ac/query/player?key=ODM5MDM4MjA3MTExMTMzOTA0MTE3NTczNzAyMDE5MDIzNTc3MTc=&player={player}")
    print(response.status_code) 
    if response.status_code == 200:
        data = response.json()
        embed=discord.Embed(description="Minecraft Alts Checker", color=0x3498db)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824386302522032159/826238837419147265/825673188032774145.png")
        embed.add_field(name="Alts", value=str(data), inline=True)
        await ctx.send(embed=embed)

        print(data)

    else:
        ctx.send("API returned a {response.status_code} status.")

@bot.command(aliases=["av"])
async def avatar(ctx, *, avamember : discord.Member=None):
    if avamember == None:
        # < =============== Animation ================= >
        juice=discord.Embed(description="Checking Avatar.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to=discord.Embed(title=f"✓", color=discord.Colour.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=to)
        await asyncio.sleep(0.30)
        await msg.delete()
        # < =============== Animation ================= >

        juice=discord.Embed(title=f"{ctx.message.author} Avatar", color=0x3498db)
        juice.set_image(url=ctx.message.author.avatar_url)
        await ctx.send(embed=juice)
        return

    # < =============== Animation ================= >
    juice=discord.Embed(description="Checking Avatar.", color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    to=discord.Embed(title=f"✓", color=discord.Colour.green())
    msg = await ctx.send(embed=juice)
    await asyncio.sleep(1)
    await msg.edit(embed=to)
    await asyncio.sleep(0.30)
    await msg.delete()
    # < =============== Animation ================= >

    userAvatarUrl = avamember.avatar_url
    ajuice=discord.Embed(title=f"{avamember} Avatar", color=0x3498db)
    ajuice.set_image(url=userAvatarUrl)
    await ctx.send(embed=ajuice)
       

@bot.command(aliases=["wi"])
async def whois(ctx, member: discord.Member = None):
    logchannel = bot.get_channel(872829031236665354)
    if not member:  
        member = ctx.message.author
    juice=discord.Embed(description="Checking User.", color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    to2=discord.Embed(title="✓", color=discord.Colour.green())
    msg = await ctx.send(embed=juice)
    await asyncio.sleep(1)
    await msg.edit(embed=to2)
    await asyncio.sleep(0.30)
    await msg.delete()   
    juice = discord.Embed(timestamp=ctx.message.created_at, title=f"User Info - {member}",  color=0x3498db)
    juice.set_thumbnail(url=member.avatar_url)
    juice.set_footer(text=f"Requested by {ctx.author}")

    juice.add_field(name="Display Name:", value=member.display_name)
    juice.add_field(name="Highest Role:", value=member.top_role.mention)
    
    juice.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    juice.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    juice.add_field(name="ID:", value=f"```{member.id}```")
    juice.set_footer(text="Who-is | ")
    await ctx.send(embed=juice)

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!whois", inline=False)
    juice2.add_field(name="Requested info for", value=member, inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | Whois")
    await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

@bot.command(aliases=["si"])
async def serverinfo(ctx):

    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    guild = ctx.guild

    # < =============== Animation ================= >
    juice=discord.Embed(description="Checking Server.", color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    to2=discord.Embed(title="✓", color=discord.Colour.green())
    msg = await ctx.send(embed=juice)
    await asyncio.sleep(1)
    await msg.edit(embed=to2)
    await asyncio.sleep(0.30)
    await msg.delete()   
    # < =============== Animation ================= >
    
    juice2 = discord.Embed(timestamp=ctx.message.created_at, color=0x3498db)
    juice2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    juice2.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)
    juice2.add_field(name='Number Of roles', value=str(role_count), inline=False)
    juice2.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
    juice2.add_field(name="Number Of Text channels", value=len(guild.channels), inline=True)
    juice2.add_field(name="Number Of Voice channels", value=len(guild.voice_channels), inline=True)
    juice2.add_field(name="Boosters", value=guild.premium_subscription_count, inline=False)
    juice2.add_field(name="Region", value=guild.region, inline=True)
    juice2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    juice2.set_thumbnail(url=ctx.guild.icon_url)
    juice2.set_author(name=f"{guild} | ID: {guild.id}", icon_url=guild.icon_url)
    juice2.set_footer(text="Server Information |")
    await ctx.send(embed=juice2)
    
    # < ======================== LOG ==================================================>
    logchannel = bot.get_channel(872829031236665354)
    juice=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice.add_field(name="Command", value=f"!serverinfo", inline=False)
    juice.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice.set_footer(text="logs | Whois")
    await logchannel.send(embed=juice)
    # < ======================== LOG ==================================================>


@bot.command(aliases=["bp"])
async def bping(ctx):

    # < =============== Animation ================= >
    juice=discord.Embed(description="Requesting Discord API", color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    to2=discord.Embed(title="✓", color=discord.Colour.green())
    msg = await ctx.send(embed=juice)
    await asyncio.sleep(1)
    await msg.edit(embed=to2)
    await asyncio.sleep(0.30)
    await msg.delete()
    # < =============== Animation ================= >

    juice3=discord.Embed(timestamp=ctx.message.created_at, title="Screenshare Bot", description="Screenshare may be 30s delayed", color=0x3498db)
    juice3.add_field(name="Ping:", value=f"```{round(bot.latency * 1000)} - ms```", inline=False)
    await ctx.send(embed=juice3)

@bot.command(aliases=["ph"])
async def phone(ctx, *,phone=None):
    logchannel = bot.get_channel(872829031236665354)
    if phone == None:
        juice=discord.Embed(description="Checking phone.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to2=discord.Embed(title="⚠️ | You dont put an phone number", color=0x3498db)
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=to2)
        return

    # < =============== Animation ================= >
    juice=discord.Embed(description="Checking phone.", color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    to2=discord.Embed(title="✓", color=discord.Colour.green())
    msg = await ctx.send(embed=juice)
    await asyncio.sleep(1)
    await msg.edit(embed=to2)
    await asyncio.sleep(0.50)
    await msg.delete() 
    # < =============== Animation ================= >
    
    phone = req.get(f"http://apilayer.net/api/validate?access_key=3cdc7d946faa9e4ad32b57efdde98c8d&number={phone}")
    data = phone.json()
    if data["valid"]:
        juice = discord.Embed(timestamp= ctx.message.created_at, color=0x3498db, description=
            f"""Valid Pone: {data["valid"]}
            Phone Number: {data["number"]}
            Local Format: {data["local_format"]}
            International Format: {data["international_format"]}
            Prefix: {data["country_prefix"]}
            Country: {data["country_code"]}
            Country Name: {data["country_name"]}
            Location: {data["location"]}
            Phone Company: {data["carrier"]}
            Line Type: {data["line_type"]}""")
        juice.set_author(name= ctx.message.author, icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed=juice)
        # < ======================== LOG ==================================================>
        juice2=discord.Embed(timestamp=ctx.message.created_at, title="[??] Logs", color=0x3498db)
        juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
        juice2.add_field(name="Command", value=f"!phone", inline=False)
        juice2.add_field(name="Also phone info", value=f"```{data}```", inline=False)
        juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
        juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
        juice2.set_footer(text="logs | Phone")
        await logchannel.send(embed=juice2)
        # < ======================== LOG ==================================================>
    else:
        juice2=discord.Embed(timestamp=ctx.message.created_at, color=0x3498db, description="Invalid phone number.")
        juice2.set_author(name= ctx.message.author, icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed=juice2)



snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@bot.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@bot.command()
async def snipe(message):
    if snipe_message_content==None:
        cum2=discord.Embed(title=" ❌ | **There is nothing to snipe**" , color=0x3498db)
        await message.channel.send(embed=cum2)
    else:
        cum=discord.Embed(title="Snipe ︻芫═──" , color=0x3498db)
        cum.add_field(name=f"Sent by: ", value=f"{snipe_message_author}")
        
        cum.add_field(name=f"Message: ", value=f"{snipe_message_content}")
        cum.set_footer(text=f"Sniped by: {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        cum.set_footer(text="Single Sniper")   
        await message.channel.send(embed=cum)
        return

@bot.command(aliases=["cnick"])
async def changenick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f"{ctx.message.author.mention} {member} was successfully renamed to {nick}")

@bot.command(aliases=["lsave"])
@has_permissions(administrator=True)
async def longsave(ctx, limit: int = 999999):
    juice=discord.Embed(color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    msg = await ctx.send(embed=juice)
    channel = ctx.message.channel
    messages = await ctx.channel.history(limit=limit).flatten()
    with open(f"{channel}_messages.txt", "a+", encoding="utf-8") as f:
        print(f"\nTranscript Saved by - {ctx.author.display_name}.\n\n", file=f)
        for message in messages:
            embed = ""
            if len(message.embeds) != 0:
                embed = message.embeds[0].description
                print(f"{message.author.name} - {embed}", file=f)
            print(f"{message.author.name} - {message.content}", file=f)
    await ctx.message.add_reaction("🧃")
    juice=discord.Embed(description="Transcript saved!", color=0x3498db)
    await ctx.send(embed=juice)
    await msg.delete()
    history = discord.File(fp=f'{channel}_messages.txt', filename=None)
    await ctx.send(file=history)

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!longsave", inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | Transcript | ⬇")
    logchannel = bot.get_channel(872829031236665354)
    await logchannel.send(embed=juice2)
    transcript = discord.File(fp=f'{channel}_messages.txt', filename=None)
    await logchannel.send(file=transcript)
    await logchannel.send("```                                       ```")
    # < ======================== LOG ==================================================>

@bot.command(aliases=["fsave"])
@has_permissions(administrator=True)
async def fastsave(ctx, limit: int = 300):
    juice=discord.Embed(color=0x3498db)
    juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
    msg = await ctx.send(embed=juice)
    channel = ctx.message.channel
    messages = await ctx.channel.history(limit=limit).flatten()
    with open(f"{channel}_messages.txt", "a+", encoding="utf-8") as f:
        print(f"\nTranscript Saved by - {ctx.author.display_name}.\n\n", file=f)
        for message in messages:
            embed = ""
            if len(message.embeds) != 0:
                embed = message.embeds[0].description
                print(f"{message.author.name} - {embed}", file=f)
            print(f"{message.author.name} - {message.content}", file=f)
    await ctx.message.add_reaction("🧃")
    juice=discord.Embed(description="Transcript saved!", color=0x3498db)
    await ctx.send(embed=juice)
    await msg.delete()
    history = discord.File(fp=f'{channel}_messages.txt', filename=None)
    await ctx.send(file=history)

    # < ======================== LOG ==================================================>
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name="Command", value=f"!fastsave", inline=False)
    juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice2.set_footer(text="logs | Transcript | ⬇")
    logchannel = bot.get_channel(872829031236665354)
    await logchannel.send(embed=juice2)
    transcript = discord.File(fp=f'{channel}_messages.txt', filename=None)
    await logchannel.send(file=transcript)
    await logchannel.send("```                                       ```")
    # < ======================== LOG ==================================================>


@bot.command()
@has_permissions(manage_messages=True)
async def poll(ctx, *, lemessage:str=None):
    if lemessage is None:

        # < =============== Animation ================= >
        juice2=discord.Embed(description="Creating Poll.", color=0x3498db)
        juice2.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        msg = await ctx.send(embed=juice2)
        await asyncio.sleep(1)
        await msg.delete()
        # < =============== Animation ================= >

        juice=discord.Embed(timestamp=ctx.message.created_at, title="Unknown poll", description="Usage: !poll (message)", color=discord.Color.gold())  
        juice.set_author(name=f"⚠ Error")
        juice.set_footer(text=f"Poll | ")
        await ctx.send(embed=juice)
    else:
    	
        # < =============== Animation ================= >
        juice=discord.Embed(description="Creating Poll.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to2=discord.Embed(title="✓", color=discord.Colour.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=to2)
        await asyncio.sleep(0.30)
        await msg.delete()
        # < =============== Animation ================= >

        juice2=discord.Embed(timestamp=ctx.message.created_at, description=f"{lemessage}", color=0x3498db)
        juice2.set_author(name=f"Poll created!")
        juice2.set_footer(text=f"Poll | ")
        reaction = await ctx.send(embed=juice2)
        await reaction.add_reaction('👍')
        await reaction.add_reaction('👎')

        # < ======================== LOG ==================================================>
        juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
        juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
        juice2.add_field(name="Command", value=f"!poll", inline=False)
        juice2.add_field(name="Poll created", value=f"{lemssage}", inline=False)
        juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
        juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
        juice2.set_footer(text="logs | Poll ")
        logchannel = bot.get_channel(872829031236665354)
        await logchannel.send(embed=juice2)
        # < ======================== LOG ==================================================>

@bot.command()
@has_permissions(manage_messages=True)
async def opoll(ctx, *, lemessage:str=None):
    if lemessage is None:

        # < =============== Animation ================= >
        juice2=discord.Embed(description="Creating Poll.", color=0x3498db)
        juice2.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        msg = await ctx.send(embed=juice2)
        await asyncio.sleep(1)
        await msg.delete()
        # < =============== Animation ================= >

        juice=discord.Embed(timestamp=ctx.message.created_at, title="Unknown poll", description="Usage: !poll (message)", color=discord.Color.gold())  
        juice.set_author(name=f"⚠ Error")
        juice.set_footer(text=f"Poll | ")
        await ctx.send(embed=juice)
    else:
        
        # < =============== Animation ================= >
        juice=discord.Embed(description="Creating Poll.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to2=discord.Embed(title="✓", color=discord.Colour.green())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=to2)
        await asyncio.sleep(0.30)
        await msg.delete()
        # < =============== Animation ================= >

        juice2=discord.Embed(timestamp=ctx.message.created_at, description=f"{lemessage}", color=0x3498db)
        juice2.set_author(name=f"Poll created!")
        juice2.set_footer(text=f"Poll | ")
        reaction = await ctx.send(embed=juice2)
        await reaction.add_reaction('1️⃣')
        await reaction.add_reaction('2️⃣')

        # < ======================== LOG ==================================================>
        juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
        juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
        juice2.add_field(name="Command", value=f"!poll", inline=False)
        juice2.add_field(name="Poll created", value=f"{lemssage}", inline=False)
        juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
        juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
        juice2.set_footer(text="logs | Poll ")
        logchannel = bot.get_channel(872829031236665354)
        await logchannel.send(embed=juice2)
        # < ======================== LOG ==================================================>

#@bot.command(aliases=["dupe"])
#async def duplicate(ctx, user : discord.User, *, message=None):
    #if message == None:
     #   await ctx.send("You need to put a message to clone this user!")
    #    return

   # await ctx.message.delete()
   # nigga =  await ctx.message.channel.create_webhook(name=user)
   # await nigga.send(message, username=user.display_name, avatar_url=user.avatar_url)
  #  await nigga.delete()
  
    # < ======================== LOG ==================================================>
   # juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
   # juice2.set_image(url=user.avatar_url)
   # juice2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
   # juice2.add_field(name="Command", value=f"!duplicate", inline=False)
   # juice2.add_field(name="Guy who has duplicated been", value=user.display_name, inline=False)
   # juice2.add_field(name="Message sent", value=message, inline=False)
  #  juice2.add_field(name="Guild", value=ctx.guild.name, inline=False)
 #   juice2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
 #   juice2.add_field(name="Duplicated User image  ⬇", value="nice image btw", inline=False)
 #   juice2.set_footer(text="logs | Duplicate ")
 #   logchannel = bot.get_channel(872829031236665354)
 #   await logchannel.send(embed=juice2)
    # < ======================== LOG ==================================================>

	
#                                <End of Utils>

#                                <Doxes>

@bot.command(aliases=["nicolew", "kiara", "pelotuda"])
async def Kiarah(ctx):
    member = ctx.message.author
    juice=discord.Embed(title="Austistic girl asf", color=0x3498db)
    juice.set_thumbnail(url="https://cdn.discordapp.com/attachments/791149140817739786/810215774156619846/54krBE4kpq.png")
    juice.set_image(url="https://cdn.discordapp.com/attachments/809247209756819466/809248273642160128/unknown-2FE10.png")
    juice.add_field(name="info", value=
    """```
    Name: Nicole Valentina Suárez
    Adress: Ruben Darío
    Adress2: esquina Mateo cortes
    City: Montevideo
    State/provincie: Departamento de Montevideo
    postal code: 12100
    Country: uruguay
    gmail: nicolevalentinasuarez2005@gmail.com
    other gmail: nicolefortnite54@gmail.com
    phone: +59 898 294092
    ```""", inline=False)
    juice.add_field(name="pics download", value="[Here](http://www.mediafire.com/file/w5rjtpp39xmzvlc/nicolew_pics.rar/file)", inline=False)
    juice.add_field(name="pirvate messages download", value="[Here](http://www.mediafire.com/file/o66aibb8uq2jywn/nicolw_dms.rar/file)", inline=False)
    juice.add_field(name="blacksquad private messages", value="[Here](http://www.mediafire.com/file/nv88lmzsu5u68on/blacksquad_priv.rar/file)", inline=False)
    juice.set_footer(text=f"")
    await member.send(embed=juice)
@bot.command(aliases=["elbypasser"])
async def enlias(ctx):
    member = ctx.message.author
    await member.send("""```
NOMBRE: Enoch Toriel Kuo Elias
DNI: 48.181.380
CUIT/CUIL: 20-48181380-9
------------------------------------------------------------------
MADRE: Yachen Kuo
REPORTAJE: https://www.youtube.com/watch?v=uRoP_i9m1cQ
------------------------------------------------------------------
PADRE: Ruben Toriel Elias
DNI: 23.507.788
CUIT/CUIL: 20-23507788-5
EDAD: 48 años
Actividad u Ocupación: Servicios de asesoramiento, dirección y gestión empresarial realizados por integrantes de los órganos de administración y/o fiscalización en sociedades anónimas
Ganancias: Activo
IVA: No Inscripto
Monotributo: B
Integra Sociedades: No
Empleador: No
Vivienda (2010): Avenida Independencia 1253 Piso 2 Departamento B Cap. Fed.-
Vivienda (2018): Miller N° 2645, 1° piso Depto “8”, CABA
------------------------------------------------------------------
HERMANA: Amanda Toriel Kuo
DNI: 45.584.273
CUIT/CUIL: 27-45584273-0
Canal De Youtube: https://www.youtube.com/watch?v=uRoP_i9m1cQ
Tiene un fetiche con los conejos con cuernos
------------------------------------------------------------------
PAIS: Argentina
CIUDAD: Buenos Aires 
ORIGEN: Taiwan
NICKS: iNotEnlias Enoch EnliasGamer
CARA: https://prnt.sc/zsh0kf
------------------------------------------------------------------
```""")

    await member.send("""```
------------------------------------------------------------------
FACEBOOK: https://www.facebook.com/100034578157777
FACEBOOK DE SU MADRE: https://www.facebook.com/1256406673
FACEBOOK DE SU PADRE: https://www.facebook.com/1158172058
FACEBOOK DE SU HERMANA: https://www.facebook.com/100004484854470
INSTAGRAM: https://www.instagram.com/inotenlias
INSTAGRAM DE SU MADRE: https://www.instagram.com/carokuo/
INSTAGRAM DE SU HERMANA: https://www.instagram.com/amanda.toriel/
CANALES: https://www.youtube.com/c/iNotEnlias https://www.youtube.com/channel/UC6KpOMJgJDqonFbXPLTenqQ
INSTAGRAM: https://www.instagram.com/inotenlias/
NEGOCIO: https://chinoargentina.org.
TWITTER: https://twitter.com/Enlias2ar/
STREAMLABS: https://streamlabs.com/enlias
DISCORD ID: 338116859020836877
------------------------------------------------------------------
```""")
@bot.command(aliases=["peruano", "koru"])
async def jappe(ctx):
    member = ctx.message.author
    juice=discord.Embed(title="Austistic peruvian guy", color=0x3498db)
    juice.set_image(url="https://cdn.discordapp.com/attachments/791149140817739786/811717167283306577/descarga_3.png")
    juice.add_field(name="info", value=
    """```
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Name: SEBASTIAN CANALES ANYOSA
    DNI: 70638613
    Country: Peru
    gmail: sebastiananyosac@gmail.com
    phone: +51 934 344 505
    Jappe: https://www.facebook.com/sebastian.anyosacanales.3
    Dad: https://www.facebook.com/michael.anyosaroman
    Mom: https://www.facebook.com/elvirarosmery.canalesramos
    dad´s cousin: https://www.facebook.com/ronald.anyosamartinez/photos 
                   Nigga Family
    https://www.facebook.com/edith.anyosa.56/photos
    https://www.facebook.com/elias.anyosa.salasar/about
    https://www.facebook.com/daniela.anyosa.7
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    https://doxbin.org/upload/DaddyJappeFreeCode
    https://ghostbin.co/paste/zf2sk
    https://streamable.com/e2lxe4

    ```""", inline=False)
    juice.add_field(name="pics download", value="[Here](http://www.mediafire.com/file/76tjg8pvqwol13n/jappe_fotos.rar/file)", inline=False)
    juice.set_footer(text=f"")
    await member.send(embed=juice)
@bot.command(aliases=["larusita", "larufarina"])
async def laru(ctx):
    member = ctx.message.author
    await member.send("""```
    Padre: Alejandro Farina (DNI: 34.454.532) Edad: 32 años
    Padre: Servicios personales n.c.p. (incluye actividades de astrología y espiritismo, las realizadas con fines sociales como agencias matrimoniales, de investigaciones genealógicas, de contratación de acompañantes, la actividad de lustrabotas, acomodadores de au
    Madre:  Mariana Rodriguez Sebedio  dni: 24.205.843 EDAD: 47 años
    Hermano: Lucas Farina (DNI: Idk)
    Laruuu: Lara Micaela Farina (DNI: 47.871.657)
    Baigorria 3054 (Direccion de su colegio primario)
    Yatay 240 (Direccion de su colegio secundario)
    ----------------------------------------------------------

    Este es el facebook de laruuu
    https://www.facebook.com/lara.farina.357

    Padre de laruuu
    https://www.facebook.com/alejandro.farina.771

    Madre de laruuu
    https://www.facebook.com/mariana.rodriguezsebedio

    Hermano de laruuu
    https://www.facebook.com/lucas.farina.79

    http://imgfz.com/i/CZKTpyd.png
    http://imgfz.com/i/lxevGKj.png    
       ```""")

@bot.command()
async def rajealgordo(ctx):
	await ctx.send("https://image.prntscr.com/image/vig_Y65BQBWHDRhDcDV0wA.png")
	
@bot.command()
async def ledox(ctx):
    member = ctx.message.author
    juice=discord.Embed(color=0x3498db)
    juice.add_field(name="dox list", value="""
    DaddyJappe: !jappe !koru !peruano
    ImNicolew: !nicolew !kiarah !pelotuda
    iNotEnlias: !elbypasser !enlias
    uwuenojado: !araya !14yo (working on it)
    LaruuMC: !laru !larusita !larufarina
        """, inline=False)
    juice.set_footer(text=f"wtf doxed people")
    await member.send(embed=juice) 

#                                <End of Funny commands>

#                                    <Interactions>

@bot.command(name="say")
async def say(ctx, *, something):
    logchannel = bot.get_channel(872829031236665354)
    if something == None:
        await ctx.send("Usage: !say (Word)")
        return
    if something == "@everyone":
        await ctx.send("Dont tag everyone :(")
        return
    if something == "@here":
        await ctx.send("Dont tag here :(")
        return
    await ctx.message.delete()    
    await ctx.send(f"**{something}**")

    # < ======================== LOG ==================================================>
    juice=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice.add_field(name="Command", value=f"!say", inline=False)
    juice.add_field(name="Also message sent", value=f"{something}", inline=False)
    juice.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice.set_footer(text="logs | Say")
    await logchannel.send(embed=juice)
    # < ======================== LOG ==================================================>


@bot.command(name="saye")
async def saye(ctx, *, something):
    logchannel = bot.get_channel(872829031236665354)
    if something == None:
        await ctx.send("Usage: !saye (Word)")
        return
    if something == "@everyone":
        await ctx.send("Dont tag everyone :(")
        return
    if something == "@here":
        await ctx.send("Dont tag here :(")
        return
    await ctx.message.delete()    
    juice = discord.Embed(title=f"{something}",  color=0x3498db)
    await ctx.send(embed=juice)

    # < ======================== LOG ==================================================>
    cum2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    cum2.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    cum2.add_field(name="Command", value=f"!saye", inline=False)
    cum2.add_field(name="Also message sent", value=f"{something}", inline=False)
    cum2.add_field(name="Guild", value=ctx.guild.name, inline=False)
    cum2.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    cum2.set_footer(text="logs | Saye")
    await logchannel.send(embed=cum2)
    # < ======================== LOG ==================================================>

@bot.command()
@has_permissions(administrator=True)
async def dm(ctx, user: discord.User, *, message=None):
    if message == None:
        juice=discord.Embed(description="An error has ocurred.", color=0x3498db)
        juice.set_author(name="Please wait", url="https://cdn.discordapp.com/attachments/812592984506892318/815471070399430676/loading-gear.gif", icon_url="https://cdn.discordapp.com/attachments/815384889368510485/815474676494368778/loading_1.gif")
        to2=discord.Embed(description="You need to put a message.", color=discord.Colour.yellow())
        msg = await ctx.send(embed=juice)
        await asyncio.sleep(1)
        await msg.edit(embed=to2)
        return
    logchannel = bot.get_channel(872829031236665354)
    message = message or "Cum"
    await ctx.message.delete()
    juice=discord.Embed(title=message, color=0x3498db)
    await user.send(embed=juice)
    juice2=discord.Embed(title=f"{user} Got messaged successfully", color=0x3498db)
    await ctx.send(embed=juice2)

    # < ======================== LOG ==================================================>
    juice3=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice3.add_field(name="Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice3.add_field(name="Command", value=f"!dm", inline=False)
    juice3.add_field(name="Also message dmed", value=f"{message}", inline=False)
    juice3.add_field(name="to user", value=f"{user}", inline=False)
    juice3.add_field(name="Guild", value=ctx.guild.name, inline=False)
    juice3.add_field(name="Guild ID", value=ctx.guild.id, inline=False)
    juice3.set_footer(text="logs | dm")
    await logchannel.send(embed=juice3)
    # < ======================== LOG ==================================================>


#                                    <End of Interactions>

#                                          <Help>
@bot.command()
async def commands(ctx):
    logchannel = bot.get_channel(872829031236665354)
    juice=discord.Embed(timestamp=ctx.message.created_at, title="", description="Commands list", color=0x3498db)
    juice.set_author(name="Screenshare", icon_url="https://cdn.discordapp.com/attachments/874385566400127097/896019949401829407/Frame_8_1.png")
    juice.add_field(name="`!moderation`", value="Shows Moderation commands", inline=False)
    juice.add_field(name="`!funny`", value="show funny commands", inline=False)
    juice.add_field(name="`!utils`", value="Show utils commands", inline=False)
    juice.add_field(name="`!inter`", value="Shows interaction commands", inline=False)
    juice.set_footer(text="Commands |")
    await ctx.send(embed=juice)
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name=f"Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name=f"Command", value=f"!commands", inline=False)
    juice2.add_field(name=f"Username", value=ctx.message.author, inline=False)
    juice2.add_field(name=f"User ID", value=ctx.message.author.id, inline=False)
    juice2.set_footer(text="logs | Commands")
    await logchannel.send(embed=juice2)

@bot.command()
async def moderation(ctx):
    logchannel = bot.get_channel(872829031236665354)
    juice=discord.Embed(timestamp=ctx.message.created_at, title="", description="Mod command list", color=0x3498db)
    juice.set_author(name="Screenshare", icon_url="https://cdn.discordapp.com/attachments/874385566400127097/896019949401829407/Frame_8_1.png")
    juice.add_field(name="`!ban`", value="Usage: !ban @user (reason)", inline=False)
    juice.add_field(name="`!unban`", value="Usage: !unban Member#0001", inline=False)
    juice.add_field(name="`!mute`", value="Usage: !mute @user (reason)", inline=False)
    juice.add_field(name="`!unmute`", value="Usage: !mute @user", inline=False)
    juice.add_field(name="`!kick`", value="Usage: !mute @kick (reason)", inline=False)
    juice.set_footer(text="Commands |")
    await ctx.send(embed=juice)
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name=f"Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name=f"Command", value=f"!mod", inline=False)
    juice2.add_field(name=f"Username", value=ctx.message.author, inline=False)
    juice2.add_field(name=f"User ID", value=ctx.message.author.id, inline=False)
    juice2.set_footer(text="logs | mod")
    await logchannel.send(embed=juice2)

@bot.command()
async def utils(ctx):
    logchannel = bot.get_channel(872829031236665354)
    juice=discord.Embed(timestamp=ctx.message.created_at, title="", description="Utils command list", color=0x3498db)
    juice.set_author(name="Screenshare", icon_url="https://cdn.discordapp.com/attachments/874385566400127097/896019949401829407/Frame_8_1.png")
    juice.add_field(name="`!Eslist`", value="Shows all server list", inline=False)
    juice.add_field(name="`!Slist`", value="Show limited server list", inline=False)
    juice.add_field(name="`!clear`", value="Usage: !clear (amount)", inline=False)
    juice.add_field(name="`!whois`", value="Usage: !whois @user (or just whois)", inline=False)
    juice.add_field(name="`!serverinfo`", value="Show server information", inline=False)
    juice.add_field(name="`!avatar`", value="Usage: !avatar @user (or just avatar)", inline=False)
    juice.add_field(name="`!phone`", value="Usage: !phone (number)", inline=False)
    juice.add_field(name="`!nuke`", value="Delete, clone channel and repos", inline=False)
    juice.add_field(name="`!fnuke`", value="Fast Delete, clone channel and repos", inline=False)
    juice.add_field(name="`!botping`", value="Show bot ping (30s delayed)", inline=False)
    juice.add_field(name="`!ip`", value="Usage: !ip (ip)", inline=False)
    juice.add_field(name="`!dns`", value="Usage: !dns (dns)", inline=False)
    juice.add_field(name="`!ping`", value="Usage: !ping (ip/host)", inline=False)
    juice.add_field(name="`!snipe`", value="Snipe latest message deleted", inline=False)
    juice.add_field(name="`!translate`", value="Usage: !translate (lang) (text)", inline=False)
    juice.add_field(name="`!save`", value="Save latest 1000 messages in a channel", inline=False)
    juice.set_footer(text="Commands |")
    await ctx.send(embed=juice)
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name=f"Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name=f"Command", value=f"!utils", inline=False)
    juice2.add_field(name=f"Username", value=ctx.message.author, inline=False)
    juice2.add_field(name=f"User ID", value=ctx.message.author.id, inline=False)
    juice2.set_footer(text="logs | utils")
    await logchannel.send(embed=juice2)

@bot.command()
async def inter(ctx):
    logchannel = bot.get_channel(872829031236665354)
    juice=discord.Embed(timestamp=ctx.message.created_at, title="", description="Interaction command list", color=0x3498db)
    juice.set_author(name="Screenshare", icon_url="https://cdn.discordapp.com/attachments/874385566400127097/896019949401829407/Frame_8_1.png")
    juice.add_field(name="`!dm`", value="Usage: !dm (user or id) (message)", inline=False)
    juice.add_field(name="`!say`", value="Usage: !say (message)", inline=False)
    juice.add_field(name="`!saye`", value="Usage: !saye (message)", inline=False)
    juice.set_footer(text="Interaction |")
    await ctx.send(embed=juice)
    juice2=discord.Embed(timestamp=ctx.message.created_at, title="[📡] Logs", color=0x3498db)
    juice2.add_field(name=f"Someone is using commands", value=f"User: {ctx.message.author}", inline=False)
    juice2.add_field(name=f"Command", value=f"!inter", inline=False)
    juice2.add_field(name=f"Username", value=ctx.message.author, inline=False)
    juice2.add_field(name=f"User ID", value=ctx.message.author.id, inline=False)
    juice2.set_footer(text="logs | utils")
    await logchannel.send(embed=juice2)


  
@bot.command()
async def help(ctx):
    juice=discord.Embed(timestamp=ctx.message.created_at, color=0x3498db)
    juice.add_field(name="How i see the commands?", value="Type !commands", inline=False)
    juice.add_field(name="Where i view the bot updates?", value="in #changelog channel", inline=False)
    juice.add_field(name="Discord invite", value="[Here](https://discord.gg/TAyRJ9PUfk)", inline=False)
    juice.add_field(name="Bot Invite", value="[Here](https://discord.com/oauth2/authorize?client_id=812146468609720371&permissions=8&scope=bot)", inline=False)
    juice.set_footer(text="Help-Center | ")
    await ctx.send(embed=juice)
    
@bot.command()
async def invite(ctx):
    juice=discord.Embed(title="Screenshare invite", description="""
    [Click me](https://discord.com/oauth2/authorize?client_id=812146468609720371&permissions=8&scope=bot)
        """ , color=0x3498db)
    juice.set_footer(text=f"Requested by: {ctx.message.author}")
    await ctx.send(embed=juice)
    # lacking owner command #    # lacking owner command #    # lacking owner command #    # lacking owner command #    # lacking owner command #    # lacking owner command #    # lacking owner command #    # lacking owner command #    # lacking owner command #

#                                          <End of Help>
# <=========================== End of commands ==============================>
bot.run("token")
