"""项目配置"""
from .utils.env import Env


# 是否debug模式
DEBUG = Env.boolean("DEBUG", False)