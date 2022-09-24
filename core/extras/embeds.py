from disnake import Embed, Colour
from core.extras.utils import score_calculator
from bs4 import BeautifulSoup

class MeEmbed:
    def __init__(self,url)->None:
        self.embed = Embed(title="About Me", color=Colour.light_grey())
        self.embed.set_thumbnail(url)
        self.embed.description = """
Hi my name is Tatsuyo,
I am a bot that has a ~~lot of~~ features about anime, manga and nsfw!

You my source code [here](https://github.com/reset-xd/Tatsuyo) *star it too while you at it*
You can invite me from [here](https://discord.com/api/oauth2/authorize?client_id=1018935891827367988&permissions=8&scope=bot%20applications.commands)
You can find my support server [here](https://discord.gg/RCCQJmqxgn)
if you dont like me then please tell me [here](https://discord.gg/RCCQJmqxgn)

for more information use the buttons!!!

`PS: I am still in development so please be patient`
"""

    def credits(self)->Embed:
        self.embed.title = "Credits"
        self.embed.description = """
**Tatsuyo** is made by resetxd#8278
Artwork taken from [twitter](https://twitter.com/luna_nyann/status/1563805450029891584/)
Made using disnake, MyanimeList, Anilist, nhentai, etc

`PS: You can get your name here by helping me!`
"""
        return self.embed

    def main(self)->Embed:
        self.embed.title = "About Me"
        self.embed.description = """
Hi my name is Tatsuyo,
I am a bot made by resetxd#8278 just for you!

You my source code [here](https://github.com/reset-xd/Tatsuyo) *star it too while you at it*
You can invite me from [here](https://discord.com/api/oauth2/authorize?client_id=1018935891827367988&permissions=8&scope=bot%20applications.commands)
You can find my support server [here](https://discord.gg/RCCQJmqxgn)
if you dont like me then please tell me [here](https://discord.gg/RCCQJmqxgn)

for more information use the buttons!!!

`PS: I am still in development so please be patient`
"""
        return self.embed

    def support(self)->Embed:
        self.embed.title = "Support"
        self.embed.description = """
You can find my support server [here](https://discord.gg/RCCQJmqxgn)
You can report bugs [here](https://discord.gg/RCCQJmqxgn)
You can suggest features [here](https://discord.gg/RCCQJmqxgn)

`PS: I am still in development so please be patient`
"""
        return self.embed

class AnimeEmbedSearch:

    def __init__(self, data)->None:
        self.data = data["data"]["Page"]["media"]
        self.embed = Embed(title="Search Results", color=Colour.light_grey())
        self.page = 0
        self.max_page = data["data"]["Page"]["pageInfo"]["total"]
        self.opened = False

    def get_search(self)->Embed:
        self.embed = Embed(title="Search Results", color=Colour.light_grey())
        if self.opened:
            return self.get_embed()
        self.embed.clear_fields()
        self.embed.title = "Search Results"

        self.embed.description = ""
        self.embed.set_thumbnail(url=self.data[self.page]["coverImage"]["extraLarge"])
        self.embed.set_footer(text=f"Page {self.page+1}/{self.max_page}")
        self.embed.add_field(name="Title", value=(self.data[self.page]["title"]["romaji"] or self.data[self.page]["title"]["native"]))
        self.embed.add_field(name="Score", value=score_calculator(int(self.data[self.page]["meanScore"] or 0)))
        self.embed.add_field(name="Type", value=(self.data[self.page]["type"] or "unknown"))
        self.embed.add_field(name="Genres", value=", ".join(self.data[self.page]["genres"]))
        self.embed.add_field(name="Status", value=(self.data[self.page]["status"] or "unknown"))
        self.embed.add_field(name="Episodes", value=(self.data[self.page]["episodes"] or "0"))
        return self.embed

    def get_embed(self)->Embed:
        self.embed = Embed(title="Search Results", color=Colour.light_grey())
        if not self.opened:
            return self.get_search()
        self.embed.clear_fields()
        self.embed.title = (self.data[self.page]["title"]["romaji"] or self.data[self.page]["title"]["native"])
        self.embed.set_thumbnail(url=self.data[self.page]["coverImage"]["extraLarge"])
        self.embed.description = str(BeautifulSoup(self.data[self.page]["description"], "html.parser").text)
        self.embed.set_footer(text=f"Page {self.page+1}/{self.max_page}")
        self.embed.add_field(name="Score", value=score_calculator(int(self.data[self.page]["meanScore"] or 0)), inline=False)
        self.embed.add_field(name="Type", value=(self.data[self.page]["type"] or "unknown"))
        self.embed.add_field(name="Genres", value=", ".join(self.data[self.page]["genres"]))
        self.embed.add_field(name="Status", value=(self.data[self.page]["status"] or "unknown"))
        self.embed.add_field(name="Episodes", value=(self.data[self.page]["episodes"] or "0"))
        self.embed.add_field(name="Season", value=(self.data[self.page]["season"] or "unkown"))
        self.embed.add_field(name="season year", value=(self.data[self.page]["popularity"] or "unkown"))
        self.embed.add_field(name="popularity", value=(self.data[self.page]["seasonYear"] or "unkown"))
        self.embed.add_field(name="date", value=f'from {(self.data[self.page]["startDate"]["year"] or "unkown")}/{(self.data[self.page]["startDate"]["month"] or "unkown")}/{(self.data[self.page]["startDate"]["day"] or "unkown")} to {(self.data[self.page]["endDate"]["year"] or "unkown")}/{(self.data[self.page]["endDate"]["month"] or "unkown")}/{(self.data[self.page]["endDate"]["day"] or "unkown")} ')
        self.embed.add_field(name="related", value=", ".join([f'[{x["title"]["romaji"]}]({x["siteUrl"]})' for x in self.data[self.page]["relations"]["nodes"]]))
        if self.data[self.page]["bannerImage"] != None:
            self.embed.set_image(url=self.data[self.page]["bannerImage"])
        return self.embed
    
    def left(self):
        if self.page > 0:
            self.page-= 1

    def right(self):
        if self.page < self.max_page-1:
            self.page+= 1
    
    def open(self):
        self.opened = not self.opened

class AnimeEmbedAniList:

    def __init__(self, data)->None:
        pass