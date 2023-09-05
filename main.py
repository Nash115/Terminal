import os,time
from colorama import Fore

def get_actual_folder():
    return os.getcwd()

def command(command):
    if command.startswith("cd "):
        path = command[3:]
        if os.path.isdir(path):
            os.chdir(path)
            return ''
        else:
            return 'cd: no such file or directory: ' + path
    os.chdir(get_actual_folder())
    return os.popen(command).read()

admin = False
if os.getpid() != 0:
    print(f"{Fore.BLUE}🛡️  Welcome administrator{Fore.YELLOW + os.getlogin() + Fore.BLUE} to the Nash115's terminal! {Fore.RESET}")
    admin = True
else:
    print(f"👋 Welcome {Fore.BLUE + os.getlogin() + Fore.RESET} to the Nash115's terminal!")

os.chdir(f"{os.path.expanduser('~')}")

cmand = ""
while True:
    if admin:
        cmand = input(f"🚀 {os.getcwd()}> ")
    else:
        cmand = input(f"{os.getcwd()}> ")
    if cmand == "exit":
        break
    for char in command(cmand):
        print(char, end='', flush=True)
        time.sleep(0.0001)
    print()
    # print(command(cmand))

print("🌇 Goodbye!")
time.sleep(1.5)