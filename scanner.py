'''
Simple Port Scanner
Adapted from:
https://www.youtube.com/watch?v=d3D8PAZV51g
***Added port range functionality
***Improved CLI ui
***Added port description
***Cleaned up code

'''

import socket
import sys
import csv

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
            p = port_def(port)
            if result == 0:
                print("Port {} is open: {}".format(port, p))
                s.close()
            else:
                print("No response on port: {}, {}".format(port, p))
                s.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C!")
        sys.exit()

    except s.error:
        print("Couldn't connect to server!")
        sys.exit()


def port_def(port):
    with open("port-list.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[1] == str(port):
                return row[2]
                break
            else:
                continue


port_scanner(host, a, b)


