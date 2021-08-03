import os
import time

print('FILER V271220')
os.system('cls')
print('\n\033[0;32;1m Shoxrux Sunnatov, Telegram: @Alexander_King\033[0m')
time.sleep(0.6)
os.system('cls')
file = str(input("\033[0;32;1m File: \033[0m"))
if file == 'help':
    print(""" Type files' names with commas(,) and type command:
    c - create
    d - delete
    r - read (Reads only first file.)
                            Shoxrux Sunnatov.
    """)
file = file.split(',')
cmd = str(input("\033[0;34;1m Command: \033[0m"))

if cmd == 'c':
    for i in range(len(file)):
        try:
            open(file[i],'x')
            print("\033[0;32;1m File created: \033[0m"+file[i])
        except:
            print("\033[0;31;1m File is already exists: \033[0m"+file[i])

elif cmd == 'd':
    for i in range(len(file)):
        try:
            os.remove(file[i])
            print("\033[0;32;1m File deleted: \033[0m"+file[i])
        except:
            print("\033[0;31;1m Unable to delete file: \033[0m"+file[i])

elif cmd == 'r':
    try:
        print(open(file[0]).read())
    except:
        print("\033[0;31;1m Unable to read file: \033[0m"+file[0])

input("\nENTER to exit...")
