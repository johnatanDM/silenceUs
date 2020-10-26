import discord
import os

token = os.getenv("tokenSilenceUs")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        servers = len(self.guilds)
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"{servers} servidores lotados de impostores")
        await self.change_presence(activity=activity)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!help' or '!ajuda':
          msg = '''
                Olá estou aqui para lhe ajudar em suas jogatinas de Among Us!
                Tenha certeza
          '''

        if message.content == '!playing' or message.content == '!p':
            #Improvement: Verify if the bot has mute permission!
            if message.author.voice and message.author.voice.channel:
                channel = message.author.voice.channel
                for member in channel.members:
                    await member.edit(mute = True)
                await message.channel.send('Shhhhhhhhh!')
            else:
                await message.channel.send("You are not connected to a voice channel")
                return


        if message.content == '!meeting' or message.content == '!m':
            if message.author.voice and message.author.voice.channel:
                channel = message.author.voice.channel
                for member in channel.members:
                    await member.edit(mute = False)
                await message.channel.send('You can speak now!')
            else:
                await message.channel.send("You are not connected to a voice channel")
                return
        

client = MyClient()
client.run(token)
