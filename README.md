# DST DEPLOY

[![DST-DEPLOY]](https://github.com/leiyi2000/dst-deploy)

## 环境说明

- `>= python3.10`
- `ubuntu22.04` (测试通过)
- `pdm`

## 环境准备

- `dpkg --add-architecture i386 && apt -y update && apt -y install lib64gcc-s1 lib64stdc++6 libcurl4-gnutls-dev`
- `apt install -y python3.10 python3-pip`

## pip安装使用

- `pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple dst-deploy`
- `python3 -c "from dst_deploy import deploy; deploy('Cluster_1')"`
- 注意：Cluster_1为存档名称，默认存放~/.klei/DoNotStarveTogether/Cluster_1

## Docker使用

- `docker build -t ubuntu:dst`
- `docker run -itd ubuntu:dst dst-server`
- `需要提前把存档拷贝到`[![dst_cluster]](./template/dst_cluster/) (注意目录层级不包含Cluster_x)

## K8S部署使用

- `kubectl apply -f k8s.yaml`
- 挂载说明
  - `steamcmd-volume` : steamcmd安装挂载
  - `server-volume` : 饥荒app安装挂载
  - `cluster-volume` : 饥荒存档挂载

## 项目修改

- `pip3 install pdm`
- `pdm config pypi.url https://pypi.tuna.tsinghua.edu.cn/simple`
- `pdm install`
- 项目运行：`pdm run dev`
- 项目打包：`pdm build`
