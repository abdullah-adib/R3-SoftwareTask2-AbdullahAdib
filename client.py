from pynput import keyboard
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 7634
s.connect((host, port))


def on_press(key):
    speed = 0
    if format(key.char) == '0':
        speed = (0 / 5) * 255
        print(f"speed has been set to {speed}")
        return speed
        s.send(key.char.encode())
    elif format(key.char) == '1':
        speed = ((1 / 5) * 255)
        print(f"speed has been set to {speed}")
        return speed
        s.send(key.char.encode())
    elif format(key.char) == '2':
        speed = (2 / 5) * 255
        print(f"speed has been set to {speed}")
        return speed
        s.send(key.char.encode())
    elif format(key.char) == '3':
        speed = (3 / 5) * 255
        print(f"speed has been set to {speed}")
        return speed
        s.send(key.char.encode())
    elif format(key.char) == '4':
        speed = (4 / 5) * 255
        print(f"speed has been set to {speed}")
        return speed
        s.send(key.char.encode())
    if format(key.char) == '5':
        speed = (5 / 5) * 255
        print(f"speed has been set to {speed}")
        return speed
        s.send(key.char.encode())
    elif format(key.char) == 'w':
        print(f"[f{speed}]" * 4)
        s.send(key.char.encode())
    elif format(key.char) == 'a':
        print(f"[r{speed}]" * 2 + f"[f{speed}]" * 2)
        s.send(key.char.encode())
    elif format(key.char) == 's':
        print(f"[r{speed}]" * 4)
        s.send(key.char.encode())
    elif format(key.char) == 'd':
        print(f"[f{speed}]" * 2 + f"[r{speed}]" * 2)
        s.send(key.char.encode())


# Collect events until released
with keyboard.Listener(
        on_press=on_press, ) as listener:
    listener.join()
