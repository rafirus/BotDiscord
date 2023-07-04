import discord
import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '/regra':
            await message.channel.send(f'{message.author.name} as regras do servidor são:\n1- Respeitar os membros.\n2- Odiar Java!\n3- Proibido pular o leg day.')
        elif message.content == '/data':
            current_date = datetime.datetime.now().strftime("%d/%m/%Y")
            await message.channel.send (f'{message.author.name}, a data atual é: {current_date}')
        elif message.content == '/hora':
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            await message.channel.send (f'{message.author.name}, a hora atual é: {current_time}')
client = MyClient(intents=intents)
client.run('MTEyNDg3NTUwNjgzMjExNzg4MQ.GfCgEp._OpecCh7NiExWUnhvceQYcqUQlHwF3u6e-qvYE')