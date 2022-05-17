import time
import comtypes
import pywinauto

path = r"C:\Users\atlas\AppData\Roaming\Spotify\Spotify.exe"
spotify = None

def start_spotify():
    global spotify

    pywinauto.Application().start(path)
    app = pywinauto.Application(backend="uia").connect(path=path)

    handle = pywinauto.findwindows.find_window(best_match="Spotify")
    spotify = app.window(handle=handle)

start_spotify()

# When program launched, do not alt-tab so user can navigate Spotify
# After ad run, alt-tab after program re-ran so window doesn't stay on screen
do_alt_tab = True

try:
    while True:
        spotify.child_window(title="Play", control_type="Button").exists(timeout=10)
        spotify.child_window(title="Play", control_type="Button").click()
        if do_alt_tab: pywinauto.keyboard.send_keys("%{TAB}")
        do_alt_tab = False

        print("waiting")
        spotify.child_window(title="Advertisement", control_type="Group").exists(timeout=3600)
        spotify.close()

        time.sleep(1)

        start_spotify()
except comtypes.COMError:
    # User closed Spotify
    exit()