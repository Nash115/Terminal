import os,time

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
    print("🛡️ Welcome administrator to the Nash115's terminal!")
    admin = True
else:
    print("👋 Welcome to the Nash115's terminal!")

os.chdir(f"{os.path.expanduser('~')}")

cmand = ""
while True:
    if admin:
        cmand = input(f"🚀 {os.getcwd()}# ")
    else:
        cmand = input(f"🚀 {os.getcwd()}> ")
    if cmand == "exit":
        break
    print(command(cmand))

print("🌇 Goodbye!")
time.sleep(1.5)