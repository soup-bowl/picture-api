import gc
import jpegdec
from urllib import urequest
from ujson import load

# This code does on the InkyPico. Change one of the segments, and set it in state.json.
# Derrived from the NASA Daily Picture sample.

gc.collect()

graphics = None
WIDTH = None
HEIGHT = None

FILENAME = "pic.jpg"

# A Demo Key is used in this example and is IP rate limited. You can get your own API Key from https://api.nasa.gov/
API_URL = "http://192.168.1.10:32420/"

# Length of time between updates in minutes.
# Frequent updates will reduce battery life!
UPDATE_INTERVAL = 60

# Variable for storing the NASA APOD Title
apod_title = None


def show_error(text):
    graphics.set_pen(4)
    graphics.rectangle(0, 10, WIDTH, 35)
    graphics.set_pen(1)
    graphics.text(text, 5, 16, 400, 2)


def update():
    global apod_title

    if HEIGHT == 448:
        # Image for Inky Frame 5.7
        IMG_URL = "https://pimoroni.github.io/feed2image/nasa-apod-daily.jpg"
    elif HEIGHT == 400:
        # Image for Inky Frame 4.0
        IMG_URL = "https://pimoroni.github.io/feed2image/nasa-apod-640x400-daily.jpg"
    elif HEIGHT == 480:
        IMG_URL = "https://pimoroni.github.io/feed2image/nasa-apod-800x480-daily.jpg"

    try:
        # Grab the image
        print(API_URL)
        socket = urequest.urlopen(API_URL)

        gc.collect()

        data = bytearray(1024)
        with open(FILENAME, "wb") as f:
            while True:
                if socket.readinto(data) == 0:
                    break
                f.write(data)
        socket.close()
        del data
        gc.collect()
    except OSError as e:
        print(e)
        show_error("Unable to download image")


def draw():
    jpeg = jpegdec.JPEG(graphics)
    gc.collect()  # For good measure...

    graphics.set_pen(1)
    graphics.clear()
    print(FILENAME)

    try:
        jpeg.open_file(FILENAME)
        jpeg.decode()
    except OSError:
        graphics.set_pen(4)
        graphics.rectangle(0, (HEIGHT // 2) - 20, WIDTH, 40)
        graphics.set_pen(1)
        graphics.text("Unable to display image!", 5, (HEIGHT // 2) - 15, WIDTH, 2)
        graphics.text("Check your network settings in secrets.py", 5, (HEIGHT // 2) + 2, WIDTH, 2)

    gc.collect()

    graphics.update()


