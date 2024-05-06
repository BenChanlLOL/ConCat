# main.py
# Author: "BenChanlLOL" on github
# Name: ConCat
# Version: 0.1
# link to github project: https://github.com/BenChanlLOL/ConCat

import socket
from sys import argv
import webbrowser


if argv:
    print("no arguments are required")

#pre defined variables
sock = socket.socket()

while True:
    address1 = input("what ip should we connect to?    ")
    if address1 == "ignore":
        break
    try:
        port1 = int(input("what port should we connect to?    "))
    except ValueError as e:
        print("Please input a real port")
    try:
        sock.connect((address1, port1))
        print("connection established")
        break
    except ConnectionRefusedError:
        print("The connection was refused")
        print("trying again")
    except socket.gaierror:
        print("input a real ip or hostname")


while True:
    cmd = input(">>>  ")
    if cmd == "exit":
        break
    elif cmd == "git-open":
        print("opening github")
        webbrowser.open('https://github.com/BenChanlLOL/ConCat')
        print("done")
    elif cmd == "bind":
        try:
            sock.bind((socket.gethostname(), 7092))
            print("starting on port 7092")
            print("server started")
        except OSError as e:
            print("Error occurred while binding socket: " + str(e))
            print("\n")
            print("perhaps run the program as sudo")
    elif cmd == "connect":
        while True:
            print("client started or message sent")
            msg = input(">>>  ")
            if msg == "exit":
                break
            sock.send("connected to your server".encode('utf-8'))
            sock.send(msg.encode('utf-8'))
            data = sock.recv(1024).decode("utf-8")
            print(data)
    elif cmd == "help" or "-h":
        usage = '''
        git-open - open github repo of the tool
        bind - start a sever
        exit - exit the tool
        connect - connect to a client and send data
        version - get the version of the tool
        help - get help
        troubleshoot - get common issues
        '''

        print("usage:\n" + usage)
    elif cmd == "version" or "-v":
        print("version: 0.1")
    elif cmd == "troubleshoot":
        print("If you are attempting to ssh using this client a BrokenPipeError is a indicator of wrong password"
              "When Using SSH a small delay after the first message will occur, then echo the SSH version. "
              "Then you will have three opportunities to enter a password"
              "use 'exit' to exit the tool"
              "if you dont want to connect to a host use 'ignore'"
              )

    else:
        print('use "help" to get info')
