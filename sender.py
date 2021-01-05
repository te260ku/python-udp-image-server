import socket
import numpy as np
import cv2
from contextlib import closing

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to_send_addr = ('127.0.0.1', 9999)

# img = np.zeros([500, 500], np.uint)
img = cv2.imread('image/sample-image.jpeg')

with closing(udp):
    jpg_str = cv2.imencode('.jpeg', img)

    # 画像を分割する
    for i in np.array_split(jpg_str[1], 100):
        # 画像の送信
        udp.sendto(i.tobytes(), to_send_addr)

    # １つのデータが終了したよを伝えるために判断できる文字列を送信する
    # -> チェックするなら送信する画像のbytes数のほうがいいと思った
    udp.sendto(b'__end__', to_send_addr)
    udp.close()