# main.py
# Author: "BenChanlLOL" on github
# Name: ConCat
# Version: 0.2.3
# link to github project: https://github.com/BenChanlLOL/ConCat
# updated on 14/06/2024

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
AllowBind = False

while True:
    address1 = input("what ip should we connect to?    ")
    if address1 == "ignore":
        AllowBind = True
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
    if cmd == "git-open":
        print("opening github")
        webbrowser.open('https://github.com/BenChanlLOL/ConCat')
        print("done")
    if cmd == "bind":
        if AllowBind == True:
            for n in range(0,6):
                 print(n)
            try:
                time.sleep(1)
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
          
            msg = conn.recv(1024).decode("utf-8")
            print(msg)
        if AllowBind == False:
            print("you dont have permission to bind")
            print("OR you did not input 'ignore' when prompted for an IP to connect to")
            break
    if cmd == "status":
        if serverOn:
            print("server is running")
            print("All services are succesful")
            print("CODE: 0")
        else:
            print("server is not running")
    if cmd == "connect":
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
        break
    if cmd == "version" or "-v":
        print("version: 0.2.3")
    if cmd == "troubleshoot":
        print("If you are attempting to ssh using this client a BrokenPipeError is a indicator of wrong password"
              "When Using SSH a small delay after the first message will occur, then echo the SSH version. "
              "Then you will have three opportunities to enter a password"
              "use 'exit' to exit the tool"
              "if you dont want to connect to a host use 'ignore'"
              )

    else:
        print('use "help" to get info')
    break
