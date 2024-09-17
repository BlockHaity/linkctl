import subprocess
import sys

# 获取ADB设备信息
def get_adb_device_info():
    try:
        # 执行ADB命令，获取设备信息
        result = subprocess.run(['adb', 'devices', '-l'], capture_output=True, text=True)
        # 如果ADB命令执行失败，打印错误信息并返回None
        if result.returncode != 0:
            print("ADB命令执行失败:", result.stderr)
            return None, None
        # 将设备信息按行分割
        devices = result.stdout.splitlines()
        # 遍历设备信息
        for device in devices[1:]:
            # 如果设备信息不为空
            if device:
                # 如果设备信息中包含':5555'，则返回'wireless'
                if ':5555' in device:
                    return 'wireless'
                # 否则返回'usb'
                else:
                    return 'usb'
        # 如果没有找到设备信息，则返回None
        return None, None
    except Exception as e:
        # 如果发生错误，打印错误信息并返回None
        print("发生错误:", e)
        return None, None

# 主函数
if __name__ == '__main__':
    # 获取命令行参数
    argv1 = sys.argv[1] if len(sys.argv) > 1 else None
    # 如果命令行参数为'screenshare'
    if argv1 == 'screenshare':
        # 获取设备连接方式
        mode = get_adb_device_info()
        # 打印设备连接方式
        print('设备连接方式:',mode)
        # 导入screenshare模块
        from screenshare import screenshare
        # 如果命令行参数包含'--no-audio'
        if '--no-audio' in sys.argv:
            # 调用screenshare函数，不共享音频
            screenshare(mode, 'none', None)
        # 如果命令行参数包含'--btaudio'
        elif '--btaudio' in sys.argv:
            # 获取蓝牙地址
            btmac = sys.argv[sys.argv.index('--btaudio')+1]
            # 调用screenshare函数，使用蓝牙音频
            screenshare(mode, 'bluetooth', btmac)
        # 否则调用screenshare函数，使用sndcpy共享音频
        elif '--scrcpy-audio' in sys.argv:
            screenshare(mode, 'scrcpy', None)
        else:
            screenshare(mode, 'sndcpy', None)
    # 否则打印使用方法
    else:
        print(r'linkctl v0.0.1')
        print(r'一个基于sndcpy,scrcpy,adb的安卓互联工具')
        print(r'======================================')
        print(r'使用方法: linkctl [功能] [参数]')
        print(r'======================================')
        print(r'screenshare [参数] - 屏幕共享')
        print(r'        --no-audio - 不共享音频')
        print(r'        --btaudio [蓝牙地址] - 使用蓝牙音频')
        print(r'        --scrcpy-audio - 使用scrcpy音频')
        print(r'          不包含参数下使用sndcpy共享音频')
        print(r'--------------------------------------')