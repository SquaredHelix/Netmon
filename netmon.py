from os import system, name
from time import sleep
from ping3 import ping

def clear_screen():
    if (name == 'nt'):
        system('cls')
    else:
        system('clear')

formatLength = 30
timeout = 0.05

def format_print(string):
    for st in string.split(" - "):
        if (len(st) <= formatLength):
            st += ' ' * (formatLength - len(st))
            print(st, end = '')
        else:
            print(st, end = '')
    print("")

buffered_terminal = []

while True:
    clear_screen()
    file = open("network.txt")
    if not(buffered_terminal == 0):
        for string in buffered_terminal:
            format_print(string)
        buffered_terminal = []
    for host in file:
        host = host.replace('\n', '')
        if (host.startswith('#')):
            buffered_terminal.append(host.replace('#', ''))
            continue
        response = ping(host, timeout=timeout)
        if (response):
            buffered_terminal.append(host + " - UP" +  " - " + " Ping: " + str(int(response * 1000)) +  "ms")
        else:
            buffered_terminal.append(host + " - DOWN")
    file.close()
    sleep(1)