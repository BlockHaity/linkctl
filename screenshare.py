#!/usr/bin/env python3

print(r'不要独立运行')

def screenshare(mode, audiomod, btmac):
    # 导入必要的模块
    import os
    import threading
    import subprocess
    # 打印版本信息
    print(r'screenshare v0.0.1')
    # 如果音频模式为sndcpy，则启动sndcpy
    if audiomod == 'sndcpy':
        def sndcpy():
            subprocess.run([r'./sndcpy'])
        threading.Thread(target=sndcpy).start()

    # 如果音频模式为bluetooth，则发送通知并连接蓝牙
    if audiomod == 'bluetooth':
        subprocess.run([r'notify-send', r'linkctl:screenshare提醒', r'注意，你需要使用blueman,blueberry等工具提前开启a2dp以实现音频转发，本工具无法开启a2dp但是会自动连接或断联。'])
        print(r'注意，你需要使用blueman,blueberry等工具提前开启a2dp以实现音频转发，本工具无法开启a2dp但是会自动连接或断联。')
        subprocess.run(['bluetoothctl', 'scan', 'on'])
        subprocess.run(['bluetoothctl', 'connect', btmac])
    # 如果连接模式为无线，则发送通知
    if mode == 'wireless':
        print(r'你正在使用无线连接，我们建议使用有线连接以获得更好的体验。')
        subprocess.run([r'notify-send',r'linkctl:screenshare提醒',r'你正在使用无线连接，我们建议使用有线连接以获得更好的体验。'])

    if audiomod == 'scrcpy':
        subprocess.run([])
        subprocess.run(['scrcpy', '--keyboard=uhid', '--require-audio'])
    else:
        subprocess.run(['scrcpy', '--no-audio', '--keyboard=uhid'])
    # 如果音频模式为sndcpy，则关闭sndcpy
    if audiomod == 'sndcpy':
        os.system("killall -g sndcpy")
    # 如果音频模式为bluetooth，则断开蓝牙连接
    elif audiomod == 'bluetooth':
        subprocess.run(['bluetoothctl', 'disconnect', btmac])
    # 退出程序
    os._exit(0)