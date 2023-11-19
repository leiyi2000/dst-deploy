"""项目配置"""
from .utils.env import Env


# 是否debug模式
DEBUG = Env.boolean("DEBUG", False)
# steam安装路径
STEAM_PATH = Env.string("STEAM_PATH")
# dst安装位置
DST_SERVER_PATH = Env.string("DST_SERVER_PATH")
# dst appid
DST_APPID = Env.int("DST_APPID", default=343050)