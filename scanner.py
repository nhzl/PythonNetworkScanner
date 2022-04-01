'''
Simple Port Scanner
Adapted from:
https://www.youtube.com/watch?v=d3D8PAZV51g
***Added port range functionality
***Added user interface
***Cleaned up code

'''


import socket
import sys



print("WARNING: Only operate on hosts in which you have permission for!")

host = str(input("Enter host to scan!(iPv4): "))

portrange = str(input("Enter port range to scan!(ex: 255 - 500 ): "))

a, b = portrange.split('-')

a = int(a)
b = int(b)

def port_scanner(host, startport, endport):
    try:
        for port in range(a, b):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((host, port))
            if result == 0:
                print("Port {} is open".format(port))
                s.close()
            else:
                print("No response on port: {}".format(port))

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except s.error:
        print ("Couldn't connect to server")
        sys.exit()


port_scanner(host, a, b)
