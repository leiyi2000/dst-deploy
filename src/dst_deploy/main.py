"""程序入口"""
import os


def get_all_environment_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")


# 调用函数获取并打印所有环境变量
get_all_environment_variables()


print("hello dst")