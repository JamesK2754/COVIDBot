import discord_slash
import requests
import discord
import discord.utils
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
from datetime import datetime
import tweepy
import os
import authgen
import lyricsgenius
import discord_slash
from discord_slash import SlashCommand

musiclist = []
geniustoken = ""
genius = lyricsgenius.Genius(geniustoken)

# https://discord.com/oauth2/authorize?client_id=805765096517009409&scope=bot&permissions=268696640

URL = "https://covid19.gov.gg/test-results"
TOKEN = ""
client = commands.Bot(command_prefix = "£")
version = ("1.4.2")
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)

@client.event
async def on_ready():
    print("Bot is online; awaiting commands")
    
@client.command()
async def ping(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send("Guernsey COVID bot is online and functional.")
    print(f"Bot was pinged at {current_time}")

@client.command()
async def about(ctx):
    aboutembed = discord.Embed(title="About bot", description=f"- A bot built to relay the number of active COVID-19 cases in Guernsey\n- Bot by JamesK2754\n- Version {version}")
    await ctx.send(embed=aboutembed)

@client.command()
async def legacycases(ctx):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    filteredtext = soup.get_text()
    splitfiltered = filteredtext.split('\n')
    splitfiltered = list(filter(None, splitfiltered))

    await ctx.send(f'There are {splitfiltered[40]} active cases of COVID-19 in Guernsey.')
    print(f'There are {splitfiltered[40]} active cases of COVID-19 in Guernsey.')
#@slash.slash(name="cases")

@client.command()
async def cases(ctx, platform="web"):
    if platform == ("web"):
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        filteredtext = soup.get_text()
        splitfiltered = filteredtext.split('\n')
        splitfiltered = list(filter(None, splitfiltered))

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        webembed = discord.Embed(title="Active COVID-19 cases in Guernsey", description=f"There are {splitfiltered[40]} active cases of COVID-19 in Guernsey.")
        webembed.set_footer(text=f"This data was taken from covid19.gov.gg/test-results at {current_time}. Wear a mask 😷.")
        
        await ctx.send(embed=webembed)

    elif platform == ("social"):
        prefix = "We currently have"
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        tweets = api.user_timeline(screen_name="Govgg",
                                    count=100,
                                    include_rts = False,
                                    tweet_mode = 'extended'
                                    )
        tweetlist = []
        for info in tweets[:101]:
            tweetlist.append(info.full_text)
        filteredtweetlist = [x for x in tweetlist if x.startswith(prefix)]
        selectedtweet = filteredtweetlist[0]
        selectedtweet = selectedtweet.split(" ")
        socialembed = discord.Embed(title="Active COVID-19 cases in Guernsey", description=f"There are {selectedtweet[3]} active cases of COVID-19 in Guernsey.")
        socialembed.set_footer(text=f"This data was taken from @Govgg on Twitter at {current_time}. Wear a mask 😷.")
        await ctx.send(embed=socialembed)
    elif platform == ("eval"):
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        filteredtext = soup.get_text()
        splitfiltered = filteredtext.split('\n')
        splitfiltered = list(filter(None, splitfiltered))

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        prefix = "We currently have"

        tweets = api.user_timeline(screen_name="Govgg",
                                    count=100,
                                    include_rts = False,
                                    tweet_mode = 'extended'
                                    )
        tweetlist = []
        for info in tweets[:101]:
            tweetlist.append(info.full_text)
        filteredtweetlist = [x for x in tweetlist if x.startswith(prefix)]
        selectedtweet = filteredtweetlist[0]
        selectedtweet = selectedtweet.split(" ")
        evalembed = discord.Embed(title="Active COVID-19 cases in Guernsey", description=f"Acording to Twitter, there are {selectedtweet[3]} acive cases.\nAcording to gov.gg, there are {splitfiltered[40]} active cases.")
        evalembed.set_footer(text=f"This data was taken from @Govgg on Twitter and from covid19.gov.gg/test-results at {current_time}. Wear a mask 😷.")
        await ctx.send(embed=evalembed)
    else:
        await ctx.send("🛑 BONK: an error has occured. Invalid argument; may only be web, social, eval, or blank.")

@client.command()
async def bedtimestory(ctx, name="list"):
    if name == ("list"):
        liststoriesembed = discord.Embed(title="Bedtime Stories: List", description="Here are the availible stories:\n[1] The Hare & the Tortoise\n[2] The Frogs & the Ox\n[3] Belling the Cat\n[4] The Town Mouse & the Country Mouse\n[5] The Fox & the Grapes\n[6] The Wolf & the Crane\n[7] The Lion & the Mouse\n[8] The Gnat & the Bull\n[9] The Plane Tree\n[10] The Owl & the Grasshopper\nTo choose a story enter £bedtimestory X, and replace X is the number of your story show above.")
        await ctx.send(embed=liststoriesembed)
    else:
        try:
            storyfile = open(f"stories/{name}.txt", "r")
            story = storyfile.read()
            story = story.split("|")
            storyembed = discord.Embed(title=story[0], description=story[1])
            storyembed.set_footer(text="Sweet dreams, wash your hands, and wear a mask 😷.")
            storyembed.set_author(name="Source: The Library of Congress")
            await ctx.send(embed=storyembed)
        except:
            await ctx.send("🛑 BONK: an error has occured. I think you entered the story ID wrong. Run £bedtimestory to see the list of availible stories.")

@client.command()
async def lockdown(ctx, name="rules"):
    if name == ("rules"):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        LDpage = requests.get("https://covid19.gov.gg/guidance/business/lockdownupdate")
        LDsoup = BeautifulSoup(LDpage.content, 'html.parser')

        LDsouptext = LDsoup.get_text()
        LDsouplist = LDsouptext.split("\n")
        LDsouplist = list(filter(None, LDsouplist))

        lockdownembed = discord.Embed(title="Guernsey Lockdown rules", description=f"{LDsouplist[24]}\n• {LDsouplist[25]}\n• {LDsouplist[26]}\n• {LDsouplist[27]}\n• {LDsouplist[28]}")
        lockdownembed.set_footer(text=f"This data was taken from covid19.gov.gg at {current_time}. Wear a mask 😷.")
        await ctx.send(embed=lockdownembed)
        
    elif name == ("briefing"):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        breifingpage = requests.get("https://covid19.gov.gg/news/media-briefings")
        breifingsoup = BeautifulSoup(breifingpage.content, 'html.parser')
        breifingsouptext = breifingsoup.get_text()
        breifingsouplist = breifingsouptext.split("\n")
        breifingsouplist = list(filter(None, breifingsouplist))
        breifingdata = breifingsouplist[22].split(" ")

        breifingembed = discord.Embed(title="States of Guernsey COVID Briefings", description=f"The next States of Guernsey COVID briefing will be on {breifingdata[8]} {breifingdata[9]} {breifingdata[10]} at {breifingdata[12]}")
        breifingembed.set_footer(text=f"This data was taken from covid19.gov.gg at {current_time}. Wear a mask 😷.")
        
        await ctx.send(embed=breifingembed)
    else:
        await ctx.send("🛑 BONK: an error has occured. Invalid argument, may only be rules, briefing, or none.")


@client.command()
async def lyrics(ctx, *, songname):
    songname = songname.split("/")
    try:
        if len(songname) == 1:
            song = genius.search_song(songname[0])  
            #lyricembed = discord.Embed(title=f"Lyrics for {songname[0]}", description=f"{song.lyrics}")
        elif len(songname) > 1:
            song = genius.search_song(songname[0], songname[1])
            #lyricembed = discord.Embed(title=f"Lyrics for {songname[0]} by {songname[1]}", description=f"{song.lyrics}")
        string = song.lyrics
        split_string = []
        split_string = string.split("\n")
        split_string = list(filter(None, split_string))
        melded_string = (split_string[0])
        x = 1
        desclist = []
        while True:
            try:
                nxtln = int(x + 1)
                a = melded_string
                b = split_string[x]
                stringmeldlength = int(len(a)) + int(len(b))
                #print(stringmeldlength)
                #input()
                if int(stringmeldlength) > 2048:
                    #print("=== STRING SPLIT 2048 ===")
                    pt1 = melded_string
                    melded_string = (b)
                    x = x + 1
                    desclist.append(pt1)
                else:
                    melded_string = (f"{melded_string}\n{b}")
                    x = x + 1
            except:
                pt2 = melded_string
                desclist.append(pt2)
                break
        for x in range(len(desclist)):
            lyricembed = discord.Embed(title=f"Lyrics for {songname[0]} ({x+1}/{len(desclist)})", description=f"{desclist[x]}")
            await ctx.send(embed=lyricembed)
        
    except:
        await ctx.send("Please send command in like this \"£lyrics \"song\" \" or \"£lyrics \"song/artist\" \"\nIf you did this it might be that the song was not found.")

@client.command()
async def play(ctx, mode, *, song):
    if mode == "play":
        musiclist.append(song)
        if len(musiclist) > 0:
            await ctx.send(f"{song} has been added to the list, it will be played once the prior songs are done.")
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
            
        if voice and voice.is_connected():
            await voice.move_to(channel)
        
        else:
            voice = await channel.connect()
        await ctx.send(f'🎶 - Now playing {song} - 🎶')
        for x in musiclist:
            voice.play()
            os.remove("song.mp3")

    if mode in ("ls", "list"):
        musicliststring = (f"NOW: {musiclist[0]}")
        for x in musiclist:
            y = x+1
            musicliststring = f"{musicliststring}\n{musiclist[y]}"
        musiclistembed = discord.Embed(title="Music play list", description=musicliststring)
        await ctx.send(embed=musiclistembed)

    else:
        await ctx.command("🛑 BONK: an error has occured. The mode you entered is invalid.")

@client.command()
@commands.has_role("Admin")
async def drunk(ctx, member : discord.Member):
    roleg = discord.utils.get(member.guild.roles, name="Drunk monkey")
    await member.add_roles(roleg)
    await ctx.send(f"{member} is a drunk monkey.")
    

@client.command()
@commands.has_role("Admin")
async def sober(ctx, member : discord.Member):
    roleg = discord.utils.get(member.guild.roles, name="Drunk monkey")
    await member.remove_roles(roleg)
    await ctx.send(f"{member} is a sober. Booooooooooooo!")

@client.command()
async def shutdown(ctx):
    member = ctx.author
    #await ctx.message.delete()
    await ctx.send("Please enter verification code:")
    await member.create_dm()
    auth = authgen.generate("King")
    await member.dm_channel.send(auth)
    msg = await client.wait_for('message', timeout=30)
    if msg.content == auth:
        await ctx.send("Accepted.")
    else:
        await ctx.send("Unable to comply, authorization code is not valid.")

@client.command()
@commands.has_any_role("Certified Gay", "Admin")
async def nuke(ctx, member : discord.Member):
    mode=4
    await ctx.send("Bombs away!")
    for x in range(mode):
        await ctx.send(f"{member.mention}")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("🛑 BONK: an error has occured. That command was not found.")
    

client.run(TOKEN)
