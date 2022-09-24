import disnake
from disnake.ext import commands, tasks
from hentai import Utils

class Reader(disnake.ui.View):
    def __init__(self, url: str):
        super().__init__()
        self.add_item(disnake.ui.Button(label="read", url=url))

def list_spliter(list, split_value):
    pos = 0
    for x in list:
        if x.id == split_value:
            return list[:pos]
        pos += 1
    return list


class Nhentai(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.notifier.start()

    @commands.slash_command(name="nhentai", description="nsfw command!", )
    async def nsfw(self, ctx:disnake.ApplicationCommandInteraction):
        return

    @nsfw.sub_command(name="search", description="Search for a doujin!")
    async def search(self, ctx:disnake.ApplicationCommandInteraction, query:str):
        if not ctx.channel.nsfw:
            return await ctx.send(f"{ctx.author.name}-sama bak.. **HENTAI** THIS IS NOT NSFW CHANNEL.", ephemeral=True)
        

    @nsfw.sub_command(name="notify", description="get notification if a new nhentai is posted related to this tag!")
    async def notifycommand(self, ctx:disnake.ApplicationCommandInteraction, tags:str = commands.Param(description="tags to notify about [seprate tags with comma]")):
        await ctx.response.defer()
        if not ctx.channel.nsfw:
            return await ctx.send(f"{ctx.author.name}-sama bak.. **HENTAI** THIS IS NOT NSFW CHANNEL.", ephemeral=True)
        
        tag = [x.strip() for x in tags.split(",")]
        await self.client.db.update_one({"_id": ctx.author.id}, {"$set": {"tag": tag, "channel": ctx.channel.id, "last": 1}}, True)
        await ctx.send(f"**{ctx.author.name}**-sama, I will notify you if a new doujin is posted with the tags: {tags}", ephemeral=True)


    @tasks.loop(seconds=5)
    async def notifier(self):
        nhentai = Utils.get_homepage()
        nhentai = nhentai.new_uploads
        data = self.client.db.find({})
        data = await data.to_list(length=1000)
        for user in data:
            userlast = list_spliter(nhentai, user["last"])
            userlast = userlast[::-1]
            for nh in userlast:
                check = any(x in user["tag"] for x in nh.tag)
                view = Reader(nh.url)
                if check:
                    embed = disnake.Embed(title=nh.title(), description="", color=disnake.Colour.dark_grey())
                    embed.set_thumbnail(url=nh.thumbnail)
                    embed.add_field(name="tags", value=f"`{'` `'.join([x.name for x in nh.tag])}`")   
                    embed.add_field(name="language", value=f"`{'` `'.join([x.name for x in nh.language])}`")   
                    embed.add_field(name="artist", value=f"`{'` `'.join([x.name for x in nh.artist])}`")      
                    user1 = await self.client.fetch_user(user["_id"])
                    try:
                        await user1.send(embed=embed, view=view)
                        await self.client.db.update_one({"_id": user1.id}, {"$set": {"last": nh.id}}, True)
                    except:
                        channel: disnake.TextChannel = await self.client.fetch_channel(user["channel"])
                        await channel.send(
                            f"{user1.mention}",
                            embed=embed, view=view
                        )
                        await self.client.db.update_one({"_id": user1.id}, {"$set": {"last": nh.id}}, True)
def setup(client):
    client.add_cog(Nhentai(client))