#!env python3
import socket
import sys

class NetCat(object):
    def bind(self, lport, lhost = ''):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((lhost, lport))
        print("bind on %d" % lport, file=sys.stderr)
        s.listen(1)
        conn, addr = s.accept()
        print('connected by %s:%d' % addr, file=sys.stderr)
        while True:
            data = conn.recv(1024)
            if not data: break
            print(data)

        print('connecting close.', file=sys.stderr)
        conn.close()

if len(sys.argv) > 1:
    lport = int(sys.argv[1])

    nc = NetCat()
    if len(sys.argv) > 2:
        lhost = sys.argv[2]
        nc.send(lport, lhost)
    else:
        nc.bind(lport)
else:
    print('''The "nc" implementation
bind: netcat.py 8000
send: netcat.py 8000 1.2.3.4''')
