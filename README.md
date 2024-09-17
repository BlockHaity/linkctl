# Linkctl

一个linux与android实现互联的命令行py脚本（搭配kde connect使用更佳）

## 已经实现的功能

### screenshare - 屏幕共享

需要`adb`,`scrcpy`,`vlc`,`bluez-utils`软件包

在archlinux上使用以下命令安装
``` bash
sudo pacman -S android-tools scrcpy vlc bluez-utils
```

但是，如果你不使用其他音频支持（或者根本不用音频），你可以删去部分包

只使用sndcpy音频，可以不安装`bluez-utils`

只使用蓝牙音频，可以不安装`vlc`

screenshare实现了类似华为多屏协同的功能，连接时除了可以镜像屏幕转发音频（可选），还可以调用手机端输入法来进行输入（以补全kde connect在控制时无法输入中文的缺陷）

*~~所以华为你为啥不行，以uhid方式嵌入键盘就行了啊~~*

#### screenshare 可能会实现的功能

- [ ] 电脑摄像头转发到手机
- [ ] 收到手机通知时，转发到电脑。并支持电脑端点击通知时自动打开screenshare并跳转到activites（不太可能去实现，毕竟kde connect已经实现通知转发了）
- [ ] 电脑端连接时发送通知到手机

## 使用方法
```
linkctl v0.0.1
一个基于sndcpy,scrcpy,adb的安卓互联工具
======================================
使用方法: linkctl [功能] [参数]
======================================
screenshare [参数] - 屏幕共享
        --no-audio - 不共享音频
        --btaudio [蓝牙地址] - 使用蓝牙音频
        --scrcpy-audio - 使用scrcpy音频
          不包含参数下使用sndcpy共享音频
--------------------------------------
```