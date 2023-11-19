"""环境变量加载工具"""
import os


class Env:
    """env加载工具"""

    @classmethod
    def string(cls, key: str, default: str) -> str:
        """加载环境变量为string"""
        return os.getenv(key, default=default)
    
    @classmethod
    def boolean(cls, key: str, default: bool) -> bool:
        """加载环境变量为bool"""
        value = os.getenv(key)
        if value is None:
            return default
        elif value == "True":
            return True
        elif value == "False":
            return False
        else:
            raise RuntimeError(f"env: {key} is not a valid boolean value")
