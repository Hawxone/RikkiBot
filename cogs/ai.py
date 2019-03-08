from discord.ext import commands
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('RikkiBot')


corpus = ChatterBotCorpusTrainer(chatbot)
list = ListTrainer(chatbot)



list.train([
    "Kontol",
    "Lo kontol",
    "Siapa tuhanmu?",
    "saya, Rikki"
])

corpus.train(
    "chatterbot.corpus.indonesia"
)

class ChatterBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog is Ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("user {} has sent a message".format(message.author))
        if message.content.startswith('bot'):
            new_input = message.content[4:]
            response = chatbot.get_response(new_input)
            msg = response
            await message.channel.send(msg)

    @commands.command()
    async def mee(self, msg):
        await msg.send("ME")



# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(ChatterBot(bot))