# Prusacam
A simple python script that lets you use a Raspberry Pi camera with Prusa Connect.

The script uses the `picamera2` library. Compatability with older hardware is possible and would require some small modifications.

Not affiliated with Prusa.

## Setup
- Clone the repo
- Get a token (these instructions may change as the Prusa Conenct site is updated)
    - Visit https://connect.prusa3d.com and log in
    - Go to the "Camera" tab
    - Click "Add new other camera" and refresh the page
    - Copy the token
- Copy the `secret.py.example` file to `secret.py`
- Paste the token into the `TOKEN` string
- Come up with a fingerprint (just some unique base64 encoded string) and paste it into the `FINGERPRINT` string.

Now, you can run the camera by executing `python prusacam.py`.

You should start to see images update on the Prusa Connect site. Your printer must be turned on for the site to update.

If everything works satisfactorally, you can optionally register the script as a system service:

- `sudo nano /etc/systemd/system/prusacam.service`
- Paste the following code:
```
[Unit]
Description=Prusacam Service
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 [PATH]/prusacam/src/prusacam.py

[Install]
WantedBy=multi-user.target
```
replacing `[PATH]` with the path to the repo you cloned. For example, on my pi, the full path is `/home/pi/prusacam/src/prusacam.py`

- Reload systemctl by running `sudo systemctl daemon-reload`
- Enable the service by running `sudo systemctl enable prusacam.service`
- Start the service by running `sudo systemctl start prusacam.service`
- Check that the service is working by running `sudo systemctl status prusacam.service`

And that should be it! Images should now be appearing on the Prusacam dashboard, and the service should autostart when you power on the pi.
