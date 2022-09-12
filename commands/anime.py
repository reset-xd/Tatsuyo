import disnake
from core.extras.embeds import AnimeEmbedMAL
from core.extras.views import AnimeViewMAL
from disnake.ext import commands

class Anime(commands.Cog):
    def __init__(self, client):
        self.client:commands.Bot = client

    @commands.slash_command(name="aniem", description="Get info on your anime and more")
    async def anime_root(self, ctx:disnake.ApplicationCommandInteraction):
        return
    
    @anime_root.sub_command(name="myanimelist", description="Search for an anime")
    async def anime_mal(self, ctx:disnake.ApplicationCommandInteraction, anime_name:str=None, anime_id:int=None):
        if anime_name is None and anime_id is None:
            await ctx.send("Please provide either an anime name or id", ephemeral=True)
            return
        lookup = anime_id or anime_name
        await ctx.response.defer()





def setup(client):
    client.add_cog(Anime(client))