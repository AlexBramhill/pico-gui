from machine import Pin, lightsleep, deepsleep
from wifi import Wifi
import urequests
import time

led = Pin('LED', Pin.OUT)


def blink_led(times, interval):
    for _ in range(times):
        led.toggle()
        time.sleep_ms(interval)


def is_awake_led_flash():
    blink_led(6, 200)


def is_connected_to_wifi_led_flash():
    blink_led(4, 1000)


def wifi_error_led_flash():
    blink_led(20, 100)


def make_request():
    try:
        response = urequests.get(
            'https://api.tfl.gov.uk/Line/central/Status?formatter=json', headers={"Accept": "application/json"})
        print(response.json())
        is_connected_to_wifi_led_flash()
    except Exception as e:
        print(e)
        wifi_error_led_flash()


def connect_and_make_request():
    try:
        Wifi.connect()
        make_request()
    except Exception as e:
        print(e)
        wifi_error_led_flash()


def connect_and_make_request_and_disconnect():
    connect_and_make_request()
    Wifi.disconnect()


def check_network_connectivity_without_reconnecting():
    while True:
        # Awake state
        is_awake_led_flash()
        connect_and_make_request()

        # Transition state
        time.sleep(1)
        print('entering light sleep')
        lightsleep(1000)

        # Awoken state from light sleep
        is_awake_led_flash()
        make_request()

        # Transition state
        time.sleep(1)
        print('entering deep sleep')
        deepsleep(1000)

        # Awoken state from deep sleep
        # Awoken state from light sleep
        is_awake_led_flash()
        make_request()

        # Loop preparation
        time.sleep(1)
        print('awoken, one more time!')


def check_network_connectivity_with_reconnecting():
    while True:
        # Awake state
        is_awake_led_flash()
        connect_and_make_request_and_disconnect()

        # Transition state
        time.sleep(1)
        print('entering light sleep')
        lightsleep(1000)

        # Awoken state from light sleep
        is_awake_led_flash()
        connect_and_make_request_and_disconnect()

        # Transition state
        time.sleep(1)
        print('entering deep sleep')
        deepsleep(1000)

        # Awoken state from deep sleep
        # Awoken state from light sleep
        is_awake_led_flash()
        connect_and_make_request_and_disconnect()

        # Loop preparation
        time.sleep(1)
        print('awoken, one more time!')


check_network_connectivity_without_reconnecting()
