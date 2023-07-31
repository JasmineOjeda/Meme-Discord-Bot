import discord
import time
import nest_asyncio

# - - - - - Variables - - - - -
TOKEN = 'xxx'
CRAZY = ['Crazy?',
            'I was crazy once',
            'They locked me in a room',
            'A rubber room',
            'A rubber room with rats',
            'And rats make me crazy']
CRAZY_WAS_SENT = False

# - - - - - Setup - - - - -
nest_asyncio.apply()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# - - - - - Functionality - - - - -
@client.event
async def on_ready():
    print('We have logged IN as {0.user}'.format(client))

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
    
    # Messages the "Mets" meme when a message sent with "mets" or "met" is sent
    if (message.content.casefold().find('mets') != -1) or (message.content.casefold().find('met') != -1):
        await message.channel.send('IT\'S ABOUT DA METS :clap: BABY! :clap: LOVE DA METS! :clap: LET\'S GO :clap::clap::clap: HIT A HOME RUN BABY! :clap: C\'MOH METS! :clap:')
        
    # Messages the "Nortiplier" meme when a message sent with "Nortiplier" is sent
    if (message.content.casefold().find('nortiplier') != -1):
        await message.channel.send('Hello everybody, my name is Nortiplier and welcome to Identity V, a 1v4 asymmetrical horror game that you guys suggested, in mass, and I saw that empilydyerz played it and said it was really good… So I’m very eager to see what is up.')
        
    if (message.content.casefold().find('treat') != -1):
        await message.channel.send('TREAT??')
        
    if (message.content.find('69') != -1):
        await message.channel.send('Nice')
        
    if (message.content.casefold().find('piss me off') != -1) or (message.content.casefold().find('anger') != -1) or (message.content.casefold().find('angry') != -1) or (message.content.casefold().find('mad') != -1) or (message.content.casefold().find('angy') != -1):
        await message.channel.send('Does it anger the beast in you, buddy?')
        
    if (message.content.casefold().find('shadow wizard money gang') != -1):
        await message.channel.send('WE LOVE CASTING SPELLS!!!')
        
    if (message.content.casefold().find('are you okay') != -1) or (message.content.casefold().find('are you ok') != -1):
        await message.channel.send('No, I\'m gonna puke Diane.')
        
    if (message.content.casefold().find('meow') != -1):
        await message.channel.send('MEOW')
        
    if (message.content.casefold().find('pee') != -1):
        await message.channel.send('PISS CHAMBER, NOW')
        
client.run(TOKEN)