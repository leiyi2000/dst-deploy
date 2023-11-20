"""main"""
import logging

from .steam import init_dst_server
from .dst import DstServer
from .settings import STEAM_PATH, DST_SERVER_PATH, DST_APPID


log = logging.getLogger(__name__)


def main():
    """主函数"""
    log.info("#### dst deploy start ####")
    init_dst_server(STEAM_PATH, DST_SERVER_PATH, DST_APPID)
    dst = DstServer(DST_SERVER_PATH, cluster="Cluster_1")
    dst.run()
    log.info("#### dst server running ####")
    while True:
        try:
            # 打印master日志
            if dst.master:
                # 执行命令
                cmd = input("input cmd: ")
                cmd = f"BEGIN_CMD\n{cmd}\nEND_CMD\n"
                dst.master.communicate(cmd, timeout=5)
        except Exception as e:
            log.exception(f"err: {e}")


if __name__ == "__main__":
    main()