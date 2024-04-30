import time
import requests
import secret
from picamera2 import Picamera2

class API:
    def __init__(self, token, fingerprint):
        self.token = token
        self.fingerprint = fingerprint
        self.url = "https://webcam.connect.prusa3d.com"

    def uploadSnapshot(self):
        url = self.url + "/c/snapshot"
        headers = {
            'accept': '*/*',
            'Content-Type': 'image/jpg',
            'fingerprint': self.fingerprint,
            'token': self.token
        }
        response = None
        try:
            with open("current.jpg", 'rb') as f:
                image = f.read()
                response = requests.put(url, headers=headers, data=image, stream=True, verify=False)
        except:
            print("Error uploading image")
        return response


class Camera:
    def __init__(self):
        self.cam = Picamera2()
        self.config = self.cam.create_still_configuration(main={"size": (6000, 4000)})
        self.cam.configure(self.config)
        self.cam.start()

    def snap(self):
        self.cam.capture_file('current.jpg')
        
    def close(self):
        self.cam.close()


if __name__ == '__main__':
    timeout = 10
    running = True
    camera = Camera()
    api = API(secret.TOKEN, secret.FINGERPRINT)
    time.sleep(1)
    try:
        while running:
            camera.snap()
            resp = api.uploadSnapshot()
            time.sleep(timeout)
    except KeyboardInterrupt:
        print("\nexiting")
    camera.close()
