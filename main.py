import socket
'''
Author: "BenChanlLOL" on github
Name: ConCat
Version: 0.0.2
'''




#pre defined variables
sock = socket.socket()

while True:
    address1 = input("what ip should we connect to?    ")
    try:
        port1 = int(input("what port should we connect to?    "))
    except ValueError as e:
        print("Please input a real port")
        break
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
    elif cmd == "bind":
        try:
            port2 = int(input("what is the server's port?  "))
            sock.bind((0.0.0.0, port2))
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
    elif cmd == "version" or "-v":
        print("version: 0.0.2")
    elif cmd == "troubleshoot":
        print("If you are attempting to ssh using this client a BrokenPipeError is a indicator of wrong password")
    elif cmd == "help" or "-h":
        usage = '''
        bind - start a sever
        exit - exit the tool
        connect - connect to a client and send data
        version - get the version of the tool
        troubleshoot - get help
        '''

        print("usage:\n" + usage)
    else:
        print('use "help" to get info')





