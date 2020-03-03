#python2 or 3
#works for multi threading

from threading import Thread
import time, getpass, sys, telnetlib

def work(i, id, password, enable, network):

    HOST = network + str(i)

    tn = telnetlib.Telnet(HOST)

    tn.read_until("Password: ")
    tn.write(password+"\n")

    tn.write("enable\n")
    tn.write(enable+"\n")
    tn.write("\n\n")

    tn.write("terminal length 0\n"); tn.write("\n\n")
    tn.write("show ver\n");tn.write("\n\n")
    tn.write("show ip int br\n");tn.write("\n\n")
    tn.write("show cdp nei \n");tn.write("\n\n")
    tn.write("show cdp nei det\n");tn.write("\n\n")
    tn.write("show module\n");tn.write("\n\n")
    tn.write("show logg\n");tn.write("\n\n")
    tn.write("exit\n")

    with open(HOST + ".txt", 'w') as myfile:
        myfile.write(tn.read_all())
        myfile.close()

    return

if __name__ == "__main__":
    id = "admin"
    password = "cisco"
    enable = "cisco"
    network ="192.168.20."
    for i in range(0,256):
        th = Thread(target=work, name=i, args=(i, id, password, enable, network))
        th.start()
        time.sleep(0.01)

print("Now getting information from network devices. Pls, wait until time out! ")