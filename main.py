import discord
import random
import time
import re
import nest_asyncio
import sys

from functions import meow_variations, bark_variations, cheer_variation

# - - - - - Setup - - - - -
nest_asyncio.apply()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# - - - - - Variables and Functions - - - - -
TOKEN = 'xxx'
CRAZY = ['Crazy?',
            'I was crazy once',
            'They locked me in a room',
            'A rubber room',
            'A rubber room with rats',
            'And rats make me crazy']
CRAZY_WAS_SENT = False
  
# - - - - - Functionality - - - - -
@client.event
async def on_ready():
    print('We have logged IN as {0.user}'.format(client))
    print(format(client.guilds))

@client.event
async def on_message(message):
    async def FIGHT_SEQUENCE(message):
        await message.channel.send("[INSERT RPG FIGHT SEQUENCE]")
    
    if message.author == client.user:
        return
    
    if random.randint(1, 500) == 1:
        await message.channel.send("doo doooo da dee da-dumm")
    
    # "?shutdown" command: Shuts down the bot
    if message.content.startswith('?shutdown'):
        print('We have logged OUT as {0.user}'.format(client))
        await client.close()
        exit();
    
    # Loops the "Crazy?" meme whenever a message sent with "crazy" is sent
    if (message.content.casefold().find('crazy') != -1):
        global CRAZY_WAS_SENT
        if not(CRAZY_WAS_SENT):
            i = 0
            global LOOP
            LOOP = True
            CRAZY_WAS_SENT = True

            while (LOOP):
                await message.channel.send(CRAZY[i])
                time.sleep(1)

                if (i == 5):
                    i-=5
                else:
                    i+=1
                    
     # Stops the "Crazy?" meme loop when a message sent with "stop" is sent
    if (message.content.casefold().find('stop') != -1):
        CRAZY_WAS_SENT = False
        LOOP = False

    # Messages a "meow" when a message with a "meow" is sent
    if (re.search("m[mraeiouw\s]+w", message.content.casefold())):
        await message.channel.send(meow_variations())

    # Messages a "bark" when a message with a "bark" is sent
    if (message.content.casefold().find("bark") != -1) or (message.content.casefold().find("woof") != -1):
        await message.channel.send(bark_variations())
    
    # Messages a "cheer" when a message with a "cheer" is sent
    if (re.search("[wyg][aeiou][ph]*[aeiou]+[aeiou]*$", message.content.casefold())):
        await message.channel.send(cheer_variation())
    
    # Random single responses
    if (message.content.casefold().find('treat') != -1):
        await message.channel.send('TREAT??')

    if (message.content.casefold().find('mets') != -1) or (message.content.casefold().find('met') != -1):
        await message.channel.send('IT\'S ABOUT DA METS :clap: BABY! :clap: LOVE DA METS! :clap: LET\'S GO :clap::clap::clap: HIT A HOME RUN BABY! :clap: C\'MOH METS! :clap:')
        
    if (message.content.casefold().find('nortiplier') != -1):
        await message.channel.send('Hello everybody, my name is Nortiplier and welcome to Identity V, a 1v4 asymmetrical horror game that you guys suggested, in mass, and I saw that empilydyerz played it and said it was really good… So I’m very eager to see what is up.')
        
    if (message.content.find('69') != -1):
        await message.channel.send('Nice')
        
    if (message.content.casefold().find('piss me off') != -1) or (message.content.casefold().find('anger') != -1) or (message.content.casefold().find('ang[r]*y') != -1) or (message.content.casefold().find('mad') != -1):
        await message.channel.send('Does it anger the beast in you, buddy?')
        
    if (message.content.casefold().find('shadow wizard money gang') != -1):
        await message.channel.send('WE LOVE CASTING SPELLS!!!')
        
    if (message.content.casefold().find('are you okay') != -1) or (message.content.casefold().find('are you ok') != -1):
        await message.channel.send('No, I\'m gonna puke Diane.')
        
    if 'pee' in message.content.casefold().split():
        if random.randint(1, 2) == 1:
            await message.channel.send('PISS CHAMBER, NOW')
        else:
            await message.add_reaction("<:pee:1137204840934682704>")

    # Responses for when the bot is mentioned
    if client.user.mentioned_in(message):
        if (message.content.casefold().find('fight') != -1):
            await message.channel.send("Fight??")
            time.sleep(2)
            await message.channel.send("YA WANNA FIGHT BRO?? >:c")
            time.sleep(1)
            await FIGHT_SEQUENCE(message)
        elif (message.content.casefold().find('dm') != -1):
            await message.author.create_dm()
            await message.author.dm_channel.send("Wassup?")
        else:
            await message.channel.send(random.choice(["joe mama", "deez nuts", "no"]))

    # Testing dm functionality
    if (message.content.casefold().find('deez nuts') != -1):
        await message.author.create_dm()
        await message.author.dm_channel.send("joe mama")
    
    if (message.content.casefold().find('joe mama') != -1) or (message.content.casefold().find('jo mama') != -1):
        await message.author.create_dm()
        await message.author.dm_channel.send("deez nuts")
        
client.run(TOKEN)