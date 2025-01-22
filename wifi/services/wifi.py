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
        attempt = 0
        while wlan.isconnected() == False and attempt < 10:
            print('Waiting for connection...')
            sleep(1)
            attempt += 1
        if not wlan.isconnected():
            raise Exception('Failed to connect to the network')
        print(f'Connected \nNetwork config: {wlan.ifconfig()}')

    @staticmethod
    def disconnect():
        print('Disconnecting from network...')
        wlan = network.WLAN(network.STA_IF)
        wlan.active(False)
        print('Disconnected')
