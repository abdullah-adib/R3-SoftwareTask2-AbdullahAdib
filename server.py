import socket
# initialize port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 7634

s.bind((host, port))
s.listen(1)

con, addr = s.accept()
print("connected with", addr)
speed = 0   # initialize speed
while True:
    c_messg = con.recv(1024)
    # conditional statements
    if c_messg.decode() == '0':
        speed = (0 / 5) * 255
        print(f"speed has been set to 0")
    elif c_messg.decode() == '1':
        speed = ((1 / 5) * 255)
        print(f"speed has been set to 1")
    elif c_messg.decode() == '2':
        speed = (2 / 5) * 255
        print(f"speed has been set to 2")
    elif c_messg.decode() == '3':
        speed = (3 / 5) * 255
        print(f"speed has been set to 3")
    elif c_messg.decode() == '4':
        speed = (4 / 5) * 255
        print(f"speed has been set to 4")
    if c_messg.decode() == '5':
        speed = (5 / 5) * 255
        print(f"speed has been set to 5")
    if c_messg.decode() == 'w':
        print(f"[f{speed}]" * 4)
    elif c_messg.decode() == 'a':
        print(f"[r{speed}]" * 2 + f"[f{speed}]" * 2)
    elif c_messg.decode() == 's':
        print(f"[r{speed}]" * 4)
    elif c_messg.decode() == 'd':
        print(f"[f{speed}]"*2 + f"[r{speed}]" * 2)