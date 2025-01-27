import network
from time import sleep
import secrets
from wifi.errors import FailedToConnectError


class Wifi:

    @staticmethod
    def __attempt_connection():
        wlan = network.WLAN(network.STA_IF)

        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

        max_attempts = 10
        attempts = 0

        while wlan.isconnected() == False and attempts < max_attempts:
            print('Waiting for connection...')
            sleep(1)
            attempts += 1

        if not wlan.isconnected():
            raise FailedToConnectError()

    @staticmethod
    def connect():
        # Connect to WLAN
        print('Connecting to network...')
        wlan = network.WLAN(network.STA_IF)

        if Wifi.is_active() and Wifi.is_connected():
            print('Already connected')
            return

        if not Wifi.is_active():
            wlan.active(True)

        Wifi.__attempt_connection()

        print(f'Connected \nNetwork config: {wlan.ifconfig()}')

    @staticmethod
    def disconnect():
        print('Disconnecting from network...')
        wlan = network.WLAN(network.STA_IF)

        if Wifi.is_active():
            wlan.active(False)
        print('Disconnected')

    @staticmethod
    def is_active():
        wlan = network.WLAN(network.STA_IF)
        return wlan.active()

    @staticmethod
    def is_connected():
        wlan = network.WLAN(network.STA_IF)
        return wlan.isconnected()
