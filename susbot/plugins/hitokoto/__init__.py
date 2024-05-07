import asyncio

import aiohttp
from nonebot import get_plugin_config
from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="hitokoto",
    description="一言",
    usage="/一言 or /hitokoto",
    config=Config,
)

config = get_plugin_config(Config)

matcher = on_command("一言", rule=to_me(), aliases={"hitokoto"}, block=True)


async def hitikoto() -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://v1.hitokoto.cn") as resp:
                r = await asyncio.wait_for(resp.json(), timeout=5)
                return f'{r["hitokoto"]}\n----{r["from"]}[{r["from_who"]}]'
    except asyncio.TimeoutError:
        return "Sorry, hitokoto timed out"


@matcher.handle()
async def _():
    await matcher.finish(await hitikoto())
