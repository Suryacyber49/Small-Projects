from pwn import *
import sys

if len(sys.argv) == 2:
    wanted_hash = sys.argv[1]
else:
    wanted_hash = input("Enter the SHA256 hash to crack: ").strip()

password_file = "Hacking python\\top-20-common-SSH-passwords.txt"
attempts = 0 

with log.progress("attempting to crack: {}!\n".format(wanted_hash)) as p:
    with open(password_file, "r", encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password) # type: ignore
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
            if password_hash == wanted_hash:
                p.success("password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
                exit()
            attempts += 1

    p.failure("password hash is not found!")