import disnake
from core.extras.embeds import AnimeEmbedSearch
from core.extras.views import  AnimeViewSearch
from disnake.ext import commands
from core.apis.anilist import search as anisearch

class Anime(commands.Cog):
    def __init__(self, client):
        self.client:commands.Bot = client

    @commands.slash_command(name="anime", description="Get info on your anime and more")
    async def anime_root(self, ctx:disnake.ApplicationCommandInteraction):
        return
    
    @anime_root.sub_command(name="search", description="Search for an anime")
    async def anime_search(self, ctx:disnake.ApplicationCommandInteraction, anime_name:str):
        await ctx.response.defer()
        
        data = await anisearch(anime_name)
        embed = AnimeEmbedSearch(data)
        view = AnimeViewSearch(embed)

        await ctx.send(embed=embed.get_search(), view=view)

def setup(client):
    client.add_cog(Anime(client))