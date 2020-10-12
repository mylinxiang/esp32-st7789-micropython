# esp32-st7789-micropython
ESP32驱动st7789 1.3寸IPS 240*240显示带图片背景时钟，micropython语言编写，带电脑端背景图片推送程序

使用步骤:
  1.main.py是micropython程序，你需要自己填好WIFI账号和密码，需要用upycraft上传至你的esp32目录。
  2.将girl.bin上传至ESP32，然后RESET设备。
  2.update.py是windows推送背景程序，需要电脑安装python3.0及以上才能运行，首次使用需要在程序中填入esp32的局域网IP地址。
