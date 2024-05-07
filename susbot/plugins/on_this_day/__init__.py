import asyncio

import aiohttp
from nonebot import get_plugin_config
from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="on_this_day",
    description="Today in history",
    usage="/历史上的今天 or /history",
    config=Config,
)

config = get_plugin_config(Config)

matcher = on_command("历史上的今天", rule=to_me(), aliases={"history"}, block=True)


async def history() -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://xiaoapi.cn/API/lssdjt.php") as resp:
                return await asyncio.wait_for(resp.text(), timeout=5)
    except asyncio.TimeoutError:
        return "Sorry, on-this-day timed out"


@matcher.handle()
async def _():
    await matcher.finish(await history())
