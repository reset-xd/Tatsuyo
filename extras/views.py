from disnake.ui import View, button
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
