# -*- coding: utf-8 -*-
# @Time    : 2024/5/7 下午8:09
# @Author  : 之落花--falling_flowers
# @File    : bot.py
# @Software: PyCharm
import nonebot
from nonebot.adapters.onebot.v12 import Adapter


def main():
    nonebot.init()
    driver = nonebot.get_driver()
    driver.register_adapter(Adapter)

    nonebot.load_builtin_plugin("echo")
    nonebot.load_plugins("susbot/plugins")
    nonebot.run()


if __name__ == '__main__':
    main()
