git pull

./gethost-SS.py
./ss2ssr.py -j ../../ShadowsocksR-win-4.9.2/gui-config.json
./gethost-V2Ray.py
./mergefile.py
./gethost-jj.py
./sendmail.py

git add .
git commit -m "Daily Update !"
git push
