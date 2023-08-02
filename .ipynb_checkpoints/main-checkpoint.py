import discord
import random
import time
import re
import nest_asyncio

# - - - - - Setup - - - - -
nest_asyncio.apply()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# - - - - - Variables and Functions - - - - -
TOKEN = 'MTEzNTI4MDAyOTg2NjEzOTcwOQ.GnQ_eV.3-WbHM4uYMfutcoPqOHzqsPD_lEPEDDI0R2mbg'
CRAZY = ['Crazy?',
         'I was crazy once',
         'They locked me in a room',
         'A rubber room',
         'A rubber room with rats',
         'And rats make me crazy']
TREAT = ['. . .',
         'Treat??',
         ':( ?',
         '. . . treat?',
         'Treeeeaaatttt']
CRAZY_WAS_SENT = False
CRAZY_CHANNEL = ""
TREAT_WAS_SENT = False
TREAT_CHANNEL = ""
#NO_TREAT_WAS_SENT = False
#NO_TREAT_COUNT = 0

def meow_variations():
    choice = random.choice([1, 1, 2, 2, 3])
    
    if (choice == 1):
        return random.choice(["MEOW", "meow", "MEOW", "meow", "*miau*"])
    if (choice == 2):
        R = ("r" * random.randint(0, 3)) 
        E = ("e" * random.randint(0, 3))
        O = (random.choice(["o", "o", "ow"]) * random.randint(1, 5))
        W =("w" * random.randint(1, 5))
        meow_variate = "m" + R + E + O + W
        
        if (random.randint(1, 2) == 1):
            meow_variate.upper()
        return meow_variate
    if (choice == 3):
        return bark_variations()
    
def bark_variations():
    bark_variate = ""
    repeat = random.randint(1, 15)
    while (repeat > 0):
        repeat-=1
        bark_variate = bark_variate + random.choice(["BARK ", "WOOF ", "BARK ", "WOOF ", ("R" * random.randint(5, 15)) + " "])
    return bark_variate
    
# - - - - - Functionality - - - - -
@client.event
async def on_ready():
    print('We have logged IN as {0.user}'.format(client))
    #text_channel_list = []
    #for guild in client.guilds:
    #    for channel in client.channels:
    #        text_channel_list.append(channel)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # "?shutdown" command: Shuts down the bot
    if message.content.startswith('?shutdown'):
        print('We have logged OUT as {0.user}'.format(client))
        await client.close()
        exit();  
    
    # Loops the "Crazy?" meme whenever a message sent with "crazy" is sent
    if (message.content.casefold().find('crazy') != -1):
        global CRAZY_WAS_SENT, CRAZY_CHANNEL
        if not(CRAZY_WAS_SENT):
            i = 0
            global CRAZY_LOOP
            CRAZY_LOOP = True
            CRAZY_WAS_SENT = True
            CRAZY_CHANNEL = message.channel.id

            while (CRAZY_LOOP):
                await message.channel.send(CRAZY[i])
                time.sleep(1)

                if (i == 5):
                    i-=5
                else:
                    i+=1
                    
    # Stops the "Crazy?" meme loop when a message sent with "stop" is sent
    if (message.content.casefold().find('stop') != -1) or (message.content.casefold().find('shut') != -1):
        if (message.channel.id == CRAZY_CHANNEL):
            CRAZY_WAS_SENT = False
            CRAZY_LOOP = False
                    
    # Sends a "meow" or occasional "barking" when a "meow" is sent
    if (re.search("m[mraeiouw\s]+w", message.content.casefold())):
        await message.channel.send(meow_variations())
    
    # Sends "barking" when a "bark" is sent
    if (message.content.casefold().find('bark') != -1) or (message.content.casefold().find('woof') != -1):
        await message.channel.send(bark_variations())
    
    # "Treat" meme
    global TREAT_WAS_SENT, TREAT_CHANNEL
    if not(TREAT_WAS_SENT) and (message.content.casefold().find('treat') != -1):
        await message.channel.send('TREAT??')
        time.sleep(2)
        if not(TREAT_WAS_SENT):
            TREAT_WAS_SENT = True
            TREAT_CHANNEL = message.channel.id
            global TREAT_LOOP
            TREAT_LOOP = True

            while (TREAT_LOOP):
                await message.channel.send(random.choice(TREAT))
                time.sleep(random.randint(2, 5))
                
    # Stops the "Treat" meme
    if (message.content.casefold().find('no treat') != -1):
        if (message.channel.id == TREAT_CHANNEL):
            TREAT_WAS_SENT = False
            TREAT_LOOP = False
            await message.channel.send("awwwwww...")
        return
                           
    #    if not(TREAT_LOOP) and (NO_TREAT_WAS_SENT):
    #        TREAT_WAS_SENT = False
    #        NO_TREAT_WAS_SENT = False
    #        await message.channel.send('awwwwwwww...')
    #        return
    #    if (TREAT_WAS_SENT) and (message.channel.id == TREAT_CHANNEL):
    #        TREAT_LOOP = False
    #        global NO_TREAT_WAS_SENT
    #        NO_TREAT_WAS_SENT = True
    #        await message.channel.send('TREAT??')
    
    # Messages the "Mets" meme when a message sent with "mets" or "met" is sent
    if (message.content.casefold().find('mets') != -1) or (message.content.casefold().find('met') != -1):
        await message.channel.send('IT\'S ABOUT DA METS :clap: BABY! :clap: LOVE DA METS! :clap: LET\'S GO :clap::clap::clap: HIT A HOME RUN BABY! :clap: C\'MOH METS! :clap:')
        
    # Messages the "Nortiplier" meme when a message sent with "Nortiplier" is sent
    if (message.content.casefold().find('nortiplier') != -1):
        await message.channel.send('Hello everybody, my name is Nortiplier and welcome to Identity V, a 1v4 asymmetrical horror game that you guys suggested, in mass, and I saw that empilydyerz played it and said it was really good… So I’m very eager to see what is up.')
        
    if (message.content.find('69') != -1):
        await message.channel.send('Nice')
        
    if (message.content.casefold().find('piss me off') != -1) or (message.content.casefold().find('anger') != -1) or (message.content.casefold().find('angry') != -1) or (message.content.casefold().find('mad') != -1) or (message.content.casefold().find('angy') != -1):
        await message.channel.send('Does it anger the beast in you, buddy?')
        
    if (message.content.casefold().find('shadow wizard money gang') != -1):
        await message.channel.send('WE LOVE CASTING SPELLS!!!')
        
    if (message.content.casefold().find('are you okay') != -1) or (message.content.casefold().find('are you ok') != -1):
        await message.channel.send('No, I\'m gonna puke Diane.')
        
    if (message.content.casefold().find('pee') != -1):
        await message.channel.send('PISS CHAMBER, NOW')
        
client.run(TOKEN)