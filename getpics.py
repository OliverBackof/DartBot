try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2

url = "http://192.168.0.8:8090/grab.jpg?oid=1&size=1080x780"
print("Bilder werden gemacht")

import cv2

def makeJPG(path,port):
    camera_port = port
    camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 780)
    print("Leere Dartscheibe wird fotografiert")
    return_value, image = camera.read()
    cv2.imwrite(path, image)

makeJPG(r"C:\Users\dasbi\OneDrive\Desktop\Pythonprojekte\Dart Automat\Test Bilder\Seite_0.jpg",3)
makeJPG(r"C:\Users\dasbi\OneDrive\Desktop\Pythonprojekte\Dart Automat\Test Bilder\Unten_0.jpg",0)
print("Wirf den Dart")
input("Enter zum fortfahren")
print("Bilder werden gemacht")
makeJPG(r"C:\Users\dasbi\OneDrive\Desktop\Pythonprojekte\Dart Automat\Test Bilder\Seite_1.jpg",3)
makeJPG(r"C:\Users\dasbi\OneDrive\Desktop\Pythonprojekte\Dart Automat\Test Bilder\Unten_1.jpg",0)
