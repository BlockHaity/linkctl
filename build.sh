#!/usr/bin/env bash

echo 'linkctl build start'
chmod 777 ./
#安装打包器
pip install pyinstaller
#生成额外依赖列表
touch imports.txt
pip freeze > imports.txt
#开始打包
yes y | pyinstaller --hidden-import=@imports.txt main.py
#补全文件
cp ./sndcpy dist/main/sndcpy
cp ./sndcpy.apk dist/main/sndcpy.apk
#重命名
mv dist/main/main dist/main/linkctl
#封装到zip
cd dist/main/
zip -r linkctl.zip *
mv linkctl.zip ../../linkctl.zip
cd ../../
#清理
rm imports.txt
echo 'linkctl build finish'