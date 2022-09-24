from disnake.ext import commands
import dotenv
import os
import disnake
import motor.motor_asyncio

dotenv.load_dotenv(".env")

# region [Constants]
client = commands.Bot(reload=True, intents=disnake.Intents().all(),test_guilds=[int(os.getenv("test_guild"))])
client.db = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("database_key"))
client.db = client.db["nofity"]["data"]

token = os.getenv("discord_token")
# endregion [Constants]

# region [Events]
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
# endregion [Events]

client.load_extensions(f"commands")

client.run(token)