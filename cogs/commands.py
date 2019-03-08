import discord
from discord.ext import commands


class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command(name='ping')
    async def ping(self,ctx):
        await ctx.send('pong!')

    @commands.command(name='clear', aliases=['bersih'])
    async def clear(self,ctx, *,amount=100):
        channel = ctx.message.channel
        messages = []
        async for message in discord.abc.Messageable.history(channel, limit=int(amount) + 1):
            messages.append(message)
        await channel.delete_messages(messages)
        await ctx.send('messages deleted.')

    @commands.command(name='repeat', aliases=['copy','mimic'])
    async def do_repeat(self, ctx, *, our_input: str):

        await ctx.send(our_input)

    @commands.command(name='help')
    async def help(self, ctx):
        await ctx.send('```nigga```')

    @commands.command(name='embeds')
    @commands.guild_only()
    async def example_embed(self, ctx):
        """A simple command which showcases the use of embeds.
        Have a play around and visit the Visualizer."""

        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(CommandsCog(bot))