dev:
	pdm run dev

prod:
	pdm run prod

build:
	pdm build

run_dst_master:
	cd ~/dst_server/bin64 && ./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Master

run_dst_caves:
	cd ~/dst_server/bin64 && ./dontstarve_dedicated_server_nullrenderer_x64 -console -cluster Cluster_1 -shard Caves

publish:
	pdm build && pdm run python3 -m twine upload dist/*