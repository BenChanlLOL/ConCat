# main.py
# Author: "BenChanlLOL" on github
# Name: ConCat
# Version: 0.2
# link to github project: https://github.com/BenChanlLOL/ConCat
# updated on 14/05/2024

import socket
from sys import argv
import sys
import webbrowser
import time
import random

if len(argv) == 2:
    print("no arguments are required")
    sys.exit()


print("Welcome to ConCat")
num1 = random.randint(0, random.randint(0, 2048))
num2 = random.randint(0, random.randint(0, 2048))
num3 = random.randint(0, random.randint(0, 2048))
num4 = random.randint(0, random.randint(0, 2048))
session_code = str(num1 + num2 + num3 + num4)
print("session code is:", session_code)
#pre defined variables
sock = socket.socket()
serverOn = False

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
            for n in range(0,6):
                print(n)
                time.sleep(1)
            try:
                sock.bind((socket.gethostname(), 7092))
                print("code 0")
            finally:
                    serverOn = True
                    sock.listen(5)
                    print("listening")
                    conn, addr = sock.accept()
            if sock.accept:
                print(conn, addr)
            print("starting on port 7092")
            print("server started")
        except OSError as e:
            print("Error occurred while binding socket: " + str(e))
            print("\n")
            print("perhaps run the program as sudo")
            print("or restart the program and, when prompted for a ip and port to connect to say 'ignore'")
        while True:
            msg = conn.recv(1024).decode("utf-8")
            print(msg)
    elif cmd == "status":
        if serverOn:
            print("server is running")
            print("All services are succesful")
            print("CODE: 0")
        else:
            print("server is not running")
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
