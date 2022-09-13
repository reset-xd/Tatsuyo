from aiohttp import ClientSession
from core.extras.graphql import anime_search_query

async def search(anime:str):
    async with ClientSession() as session:
        async with session.post("https://graphql.anilist.co", json={"query": anime_search_query, "variables": {"search": anime}}) as resp:
            return await resp.json()



