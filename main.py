#!/usr/bin/env python3

import socket
import argparse

RESPONSE = """\
HTTP/1.0 200 OK

HELLO!
""".encode()


def parse_args() -> tuple[str, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", type=str, default="127.0.0.1")
    parser.add_argument("-p", "--port", type=int, default=8000)
    args = parser.parse_args()
    return args.host, args.port


def main() -> None:
    host, port = parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    print("Listening port %s" % port)
    try:
        while True:
            connection, address = sock.accept()
            print("Connection from %s" % str(address))
            # response = connection.recv(1024).decode()
            connection.sendall(RESPONSE)
            connection.close()
    except:
        raise
    finally:
        sock.close()


if __name__ == "__main__":
    main()
