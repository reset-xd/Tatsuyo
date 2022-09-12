import disnake
from extras.embeds import MeEmbed
from extras.views import MeView
from disnake.ext import commands

class AboutMe(commands.Cog):
    def __init__(self, client):
        self.client:commands.Bot = client

    @commands.slash_command(name="about-me", description="Get information about the me!", )
    async def aboutme(self, ctx:disnake.ApplicationCommandInteraction):
        x = MeEmbed(self.client.user.display_avatar.url)
        await ctx.send(embed=x.embed, view=MeView(x))

def setup(client):
    client.add_cog(AboutMe(client))