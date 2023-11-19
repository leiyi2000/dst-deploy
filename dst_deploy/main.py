"""main"""
import logging

from .steam import init_dst_server
from .settings import STEAM_PATH, DST_SERVER_PATH, DST_APPID


log = logging.getLogger(__name__)


def main():
    """主函数"""
    log.info("#### dst deploy start ####")
    init_dst_server(STEAM_PATH, DST_SERVER_PATH, DST_APPID)


if __name__ == "__main__":
    main()