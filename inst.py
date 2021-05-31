import discord
import os

Token = 'ODQ4OTE3MTYyODk4MjI3MjEw.YLTltw.W3TlJc-FdyRsX9UdRk7db2cfz_A'

client = discord.Client() 

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith('Devil'):
        await msg.channel.send("Progress undergoing Devil")

client.run(Token)
