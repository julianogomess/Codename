import discord
import asyncio
from discord.ext import commands, tasks
client = discord.Client()

class Palavra(object):
	def __init__(self, palavra):
		self.palavra = palavra
TEXTO = Palavra(' ')
@client.event
async def on_message(message):
	canal = client.get_channel(757704072722645032)
	if(message.content.find('.jogo') != -1):
		l = []
		msg = ''
		arquivo = open('spy.txt', 'r')
		l = arquivo.readlines()
		for x in l:
			msg += x

		await canal.send(msg)
	elif message.channel == canal:
		print(message.content)
		TEXTO.palavra = message.content

	#await client.logout()

def enviarPalavra():
	return TEXTO.palavra

client.run('NzU3NzMyMDE1OTM5MjU2Mzgw.X2kq7g.iDodHKv9kzMsPwi2PQ1lE8wN14c')


