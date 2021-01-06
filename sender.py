import socket
import numpy as np
import cv2
from contextlib import closing
import time
import base64

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to_send_addr = ('127.0.0.1', 12345)

img = cv2.imread('image/sample-image-2.jpeg')
# img = np.zeros((100, 100, 3))
# cv2.imwrite('blank.png',img)


with closing(udp):
    jpg_str = cv2.imencode('.jpeg', img)
    
    # 一括送信
    # data = jpg_str[1].tobytes()
    # udp.sendto(data, to_send_addr)

    # 画像を分割する
    # 3つに分けて送信する
    for i in np.array_split(jpg_str[1], 3):
        data = i.tobytes()
        udp.sendto(data, to_send_addr)
        print("send: " + str(data))
        # time.sleep(2)

    # udp.sendto(b'__end__', to_send_addr)

    udp.close()