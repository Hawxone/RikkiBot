import requests
import discord
from discord.ext import commands
from bs4 import BeautifulSoup


class Thunder(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="thunder") #>>thunder {in game name}
    async def thunder_(self, ctx, *, search: str):

        """
        Using Beautifulsoup to scrape Thunderskill player stats page
        while all texts returned in list
        """

        source = requests.get(f'https://thunderskill.com/en/stat/{search}').text
        soup = BeautifulSoup(source,'lxml')

        dossier = requests.get(f'https://thunderskill.com/en/stat/{search}/resume').text
        resume = BeautifulSoup(dossier,'lxml')




        battle_type = [] # arcade, realistic, simulator
        battle_title = [] # good player, above average, excellent player
        kd = [] # scraped data from thunderskill
        player_title = [] # the same for battle title but for overall title


        info = resume.find('div', class_='profile-info-value')

        #checks if the user exists
        if info != None:

            for data in info.find_all('span'):
                player_title = data.text

            for stat in soup.find_all('div', class_='col mycol text-center'):
                battle_type.append(stat.strong.text)
                battle_title.append(stat.find('div',class_='resume').text)

            for data in soup.find_all('span', class_='badge'):
                kd.append(data.text)
                print(data)

        else:
            await ctx.send("Can't find the user")

            return


        player_title = player_title.strip()

        avatar = resume.find('img', id='avatar')['src']


        #embeds

        embed = discord.Embed(title=f"{search}`s Stats",
                              description=f'Congratulations! {search} is a {player_title}',
                              colour=0x98FB98)
        embed.set_author(name=f'{search}',
                         url=f'https://thunderskill.com/en/stat/{search}/resume',
                         icon_url=avatar)
        embed.set_image(url=avatar)

        embed.add_field(name=f'{battle_type[0]}', value=f'Win Rate : {kd[2]}\n Kill / Death Ratio : {kd[3]}\n Frags per battle : {kd[6]}\n Lifespan : {kd[9]}\n Total battles : {kd[10]}\n {battle_title[0]}')
        embed.add_field(name=f'{battle_type[1]}', value=f'Win Rate : {kd[13]}\n Kill / Death Ratio : {kd[14]}\n Frags per battle : {kd[17]}\n Lifespan : {kd[20]}\n Total battles : {kd[21]}\n {battle_title[1]}')
        embed.add_field(name=f'{battle_type[2]}', value=f'Win Rate : {kd[24]}\n Kill / Death Ratio : {kd[25]}\n Frags per battle : {kd[28]}\n Lifespan : {kd[31]}\n Total battles : {kd[32]}\n {battle_title[2]}')
        embed.set_footer(text='Ok thats all.', icon_url='https://i.imgur.com/Vlcgbsx.png')

        await ctx.send(content=f'Here is your stats, Mr. **{kd[13]}** Win Rate. {ctx.author.mention}', embed=embed)

def setup(bot):
    bot.add_cog(Thunder(bot))