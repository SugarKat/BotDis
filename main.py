import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    
    async def on_message(self, message):
        if message.author.name == EdvinasName:
            emoji = lobsterEmote
            if emoji:
                await message.add_reaction(emoji)
        elif message.author.name == myOwnName:
            emoji = psychoEmote
            if emoji:
                await message.add_reaction(emoji)

psychoEmote = '<:psycho:830482683812380772>'
lobsterEmote = '<:bluelobster:1024303228491399199>'
myOwnName = 'Karolukas'
EdvinasName = 'mayro krat'
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('NzUyOTY2OTk0OTczNjg4MDAw.Gao-06.2wXZ0VxuzNgh0uhXDZFjCcNBtYDLG9DcXp1Mdw')