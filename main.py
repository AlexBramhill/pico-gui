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


def make_network_request():
    Wifi.connect()
    response = urequests.get(
        'https://api.tfl.gov.uk/Line/central/Status?formatter=json', headers={"Accept": "application/json"})
    print(response.json())
    Wifi.disconnect()


def check_awake_and_make_network_request():
    is_awake_led_flash()
    try:
        make_network_request()
        is_connected_to_wifi_led_flash()
    except Exception as e:
        print(e)
        wifi_error_led_flash()


while True:

    # Awake state
    check_awake_and_make_network_request()

    # Transition state
    time.sleep(1)
    print('entering light sleep')
    lightsleep(1000)

    # Awoken state from light sleep
    check_awake_and_make_network_request()

    # Transition state
    time.sleep(1)
    print('entering deep sleep')
    deepsleep(1000)

    # Awoken state from deep sleep
    check_awake_and_make_network_request()

    # Loop preparation
    time.sleep(1)
    print('awoken, one more time!')
