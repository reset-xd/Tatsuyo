from disnake.ext import commands
import dotenv
import os
import disnake

dotenv.load_dotenv(".env")

# region [Constants]
client = commands.Bot(reload=True, intents=disnake.Intents().all(),test_guilds=[int(os.getenv("test_guild"))])
token = os.getenv("discord_token")
# endregion [Constants]

# region [Events]
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
# endregion [Events]

client.load_extensions(f"commands")

client.run(token)