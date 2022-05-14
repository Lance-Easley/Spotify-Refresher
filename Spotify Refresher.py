import time
from pywinauto import Application

path = r"C:\Users\atlas\AppData\Roaming\Spotify\Spotify.exe"
spotify = None

def start_spotify():
    global spotify

    Application().start(path)
    app = Application(backend="uia").connect(path=path)

    app["Spotify Free"].exists(timeout=30)
    handle = app["Spotify Free"].handle
    spotify = app.window(handle=handle)

start_spotify()

while True:
    spotify.child_window(title="Play", control_type="Button").exists(timeout=10)
    spotify.child_window(title="Play", control_type="Button").click()
    
    print("waiting")
    spotify.child_window(title="Advertisement", control_type="Group").exists(timeout=3600)
    spotify.close()

    time.sleep(1)

    start_spotify()