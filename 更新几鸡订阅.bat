@echo off
git pull

python gethost-jj.py

git add .
git commit -m "Daily Update !"
git push

@pause