#!/usr/bin/env python3

#program to log and display NASSP CSM/LEM/IU telemetry data



if __name__ == '__main__':
    
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.19', 14242))
    a = 500
    while True:
        data = s.recv(256)
        if not data:
            break
        s.close()
        print(repr(data))
