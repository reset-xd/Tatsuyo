from disnake import Embed, Colour

class MeEmbed:
    def __init__(self,url)->None:
        self.embed = Embed(title="About Me", color=Colour.light_grey())
        self.embed.set_thumbnail(url)
        self.embed.description = """
Hi my name is Tatsuyo,
I am a bot that has a ~~lot of~~ features about anime and manga!

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
Made using disnake, MyanimeList, Anilist, etc

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