import network
from time import sleep
import secrets


class Wifi:
    @staticmethod
    def connect():
        # Connect to WLAN
        print('Connecting to network...')
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
        print(f'Connected \nNetwork config: {wlan.ifconfig()}')

    @staticmethod
    def disconnect():
        print('Disconnecting from network...')
        wlan = network.WLAN(network.STA_IF)
        wlan.active(False)
        print('Disconnected')