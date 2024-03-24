import os
import socket

HOST = "toaster.zumepro.cz"
PORT = 42069

BRIGHTNESSPATH = "/sys/class/leds/{0}/brightness"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(1024))
    s.sendall(b'GTP_4.2 CLT\r\ni_am_a_toaster\r\n')
    print(s.recv(16))

    while True:
        data = s.recv(3)
        vals = [x for x in data]
        print(data)
        print([x for x in data])

        for led in os.listdir("/sys/class/leds"):
            if led.endswith("red"):
                with open(BRIGHTNESSPATH.format(led), "w") as f:
                    f.write("%d" % vals[0])

            if led.endswith("green"):
                with open(BRIGHTNESSPATH.format(led), "w") as f:
                    f.write("%d" % (vals[1] * 4))

            if led.endswith("blue"):
                with open(BRIGHTNESSPATH.format(led), "w") as f:
                    f.write("%d" % (vals[2] * 4))
