"""环境变量加载工具"""
import os


class Env:
    """env加载工具"""

    @classmethod
    def string(cls, key: str, default: str) -> str:
        """加载环境变量为string"""
        return os.getenv(key, default=default)
