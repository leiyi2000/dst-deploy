FROM ubuntu:22.04

# 饥荒存档目录
RUN mkdir -p /root/.klei/DoNotStarveTogether/Cluster_1
# 拷贝模板存档
COPY template/dst_cluster /root/.klei/DoNotStarveTogether/Cluster_1

# 安装steamcmd需要的依赖
RUN dpkg --add-architecture i386 && apt -y update && apt -y install lib64gcc-s1 lib64stdc++6 libcurl4-gnutls-dev
# python环境
RUN apt install -y python3.10 python3-pip
# 安装部署脚本
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple dst-deploy
# 部署并启动饥荒服务
CMD ["python3", "-c", "from dst_deploy import deploy; deploy('Cluster_1')"]