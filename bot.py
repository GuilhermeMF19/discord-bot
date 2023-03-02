import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(self.user, " Is Running!")


    async def on_message(self, message):
        if message.content == '!regras':
            regras = '1. Respeitar os membros'
            regras += '\n2. Não ser preconceituoso'
            regras += '\n3. Se Divirta!'
            bemvindo = 'Seja bem-vindo! Aproveite seu tempo por aqui.'
            await message.channel.send(regras)
            await message.author.send(bemvindo)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('Coloque seu token aqui!')
