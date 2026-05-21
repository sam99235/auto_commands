#oussama mejdoubi
##a programme that listens on port 4545 and executes a cmd command from a smart phone 

#script history
#first version realsead august 18 2024  used for only for remote command execution
#last update 2/21/2026 sending key-strokes events and using multi-threading so i can quit using letter q key on the keyboard

#use cases
#presenting on powerpoint
#remote command execution

#TODO
managing firewall permission automatically
#import os
# Example: Allow a specific port (e.g., 8080) for your app
#os.system('netsh advfirewall firewall add rule name="PythonApp" dir=in action=allow protocol=TCP localport=8080')




#requirements
#python
#socket, keyboard, threading
#u need have shared network for your phone and laptop
#client device that sends commands for android 
# u can download this app or use an udp sender app of your choice
#https://play.google.com/store/apps/details?id=com.lcyu.udptcpnetworkutility

#DEV NOTES
#TO DO LIST
#SERVER CAN SEND A ACK TO THE CLIENT



import socket, keyboard, threading

#for liux keyabord needs root access or u can use add from pynput import keyboard

running = True

def listen_for_quit():
    global running

    keyboard.wait('q')
    print("q pressed, exiting...")
    srv.close()
    running = False

# start keyboard listener thread
threading.Thread(target=listen_for_quit, daemon=True).start()


##local port
PORT = 4545

###get the local IP
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

###UDP PROTOCOL
srv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

###BINDING  udp with the ADDR
srv.bind(ADDR)
print(f"socket is opend {SERVER}:{PORT}")
print("send anything to execuete commands\n" \
"f: go foward\n" \
"b: go backward")


def execute_cmd():
    data = ""
    try:
        data = srv.recv(1024)
        data = data.decode('utf-8')
        print(data)
        if data=="f":
            keyboard.press_and_release('space')
        elif data=="b":
            keyboard.press_and_release('up')
        else:
            print("send allowed commands")
    except Exception:
            pass
    

    # try:
    #     subprocess.run(data,shell=True)
    # except Exception as e:
    #     print(f'error has occured {e}')

        


while running:
    execute_cmd()

