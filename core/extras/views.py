from disnake.ui import View, button, Button
from disnake import ButtonStyle

class MeView(View):
    def __init__(self, embed):
        super().__init__()
        self.embed = embed

    @button(label="Main", style=ButtonStyle.green)
    async def main(self, button, interaction):
        await interaction.response.edit_message(embed=self.embed.main())

    @button(label="Credits", style=ButtonStyle.green)
    async def credits(self, button, interaction):
        await interaction.response.edit_message(embed=self.embed.credits())

    @button(label="Support", style=ButtonStyle.green)
    async def support(self, button, interaction):
        await interaction.response.edit_message(embed=self.embed.support())

class AnimeViewSearch(View):
    
    def __init__(self, embedclass):
        super().__init__()
        self.embed = embedclass

    @button(emoji="⏪", style=ButtonStyle.green)
    async def left(self, button, interaction):
        self.embed.left()
        await interaction.response.edit_message(embed=self.embed.get_search())

    @button(emoji="⏩", style=ButtonStyle.green)
    async def right(self, button, interaction):
        self.embed.right()
        await interaction.response.edit_message(embed=self.embed.get_search())

    @button(label="More Info", style=ButtonStyle.green)
    async def anilist(self, button, interaction):
        self.embed.open()
        await interaction.response.edit_message(embed=self.embed.get_embed())

    @button(label="Review", style=ButtonStyle.green)
    async def support(self, button, interaction):
        await interaction.response.edit_message(embed=self.embed.support())
