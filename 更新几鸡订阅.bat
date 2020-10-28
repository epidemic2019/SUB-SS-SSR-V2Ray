@echo off
git pull

python gethost-jj.py
python sendmail.py

git add .
git commit -m "Daily Update !"
git push

@pause