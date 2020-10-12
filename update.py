"""
时钟背景图片推送程序
运行环境:Windows xp以上,python3.0以上
操作方式：将转码的二进制.bin格式的文件拖放到此程序打开
注意事项：图片取模软件设置，bin格式输出，水平扫描，240*240分辨率，16位彩色，不包含图像头

"""
from socket import *
import sys


HOST = '填写你的ESP32的IP地址'

file=sys.argv[1] #获取文件路径，你也可以直接指定。
PORT = 1024
BUFSIZ =1024
ADDR = (HOST,PORT)

input("[路径]%s\n-------------------------------\n[提示]确认同步此背景文件吗? 回车即可确认。"%file)
print("[提示]已确认，正在传输数据！")
try:
        tcpCliSock = socket(AF_INET,SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        with open(file,"rb") as f:
                pos=0
                while True:
                        f.seek(pos)
                        tcpCliSock.send(f.read(480))
                        pos+=480
                        tcpCliSock.recv(BUFSIZ)
                        if pos==240*240*2:
                                break
                tcpCliSock.close()
                input("[提示]同步完成,请等待设备自动刷新")
except:
        input("[提示]同步失败，请重启设备再试！")
