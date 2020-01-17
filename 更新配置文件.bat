@echo off
git pull

python gethost-SS.py
python ss2ssr.py -j ..\..\ShadowsocksR-win-4.9.2\gui-config.json
python gethost-V2Ray.py

git add .
git commit -m "Daily Update !"
git push

python txt2url.py
cd ..\..\v2rayN-Core
python check_v2ray.py
@pause