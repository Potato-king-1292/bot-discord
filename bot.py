from email.mime import message
from turtle import mode

import discord

import password

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith(password.genera_password_base()):
         await message.channel.send("bentornato")
         mode=2



    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
w
client.run("")
@client.event
async def on_message(message):
    if mode==2:
        if message.content.startswith('$chi è online?'):
            await message.channel.send("io e te")