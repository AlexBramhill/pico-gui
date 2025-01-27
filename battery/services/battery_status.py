from machine import ADC, Pin
from battery.errors import LowVoltageError, IncorrectStateError
from wifi import Wifi
"""
Modified version of the battery_pico.py file from
https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_lipo_shim/battery_pico.py.

Note - To work with Wireless Picos, the pin outs needed to be changed.

In addition, there is an issue with wifi being enabled interacting with the reading.
To fix this, the wifi is disabled before the reading and re-enabled after the reading.

Read more: 
https://www.reddit.com/r/raspberrypipico/comments/xalach/comment/ipigfzu/

"""


class BatteryStatus:
    @staticmethod
    def __get_vsys():
        # Pico W voltage read function by darconeous on reddit:
        # https://www.reddit.com/r/raspberrypipico/comments/xalach/comment/ipigfzu/
        try:
            is_wifi_enabled_prior_to_measurement = Wifi.is_active()
            if is_wifi_enabled_prior_to_measurement:
                Wifi.disconnect()

            # Make sure pin 25 is high.
            Pin(25, mode=Pin.OUT, pull=Pin.PULL_DOWN).high()

            # Reconfigure pin 29 as an input.
            Pin(29, Pin.IN)

            return ADC(29)

        finally:
            # Restore the pin state and possibly reactivate WLAN
            Pin(29, Pin.ALT, pull=Pin.PULL_DOWN, alt=7)
            if is_wifi_enabled_prior_to_measurement:
                Wifi.connect()

    """
    This voltage reading is not accurate when the battery is charging, 
    hence providing a public method to get the voltage that has error raising
    """
    @staticmethod
    def __get_voltage():
        conversion_factor = 3 * 3.3 / 65535
        return BatteryStatus.__get_vsys().read_u16() * conversion_factor

    @staticmethod
    def get_voltage():
        if BatteryStatus.is_charging():
            raise IncorrectStateError("Charging", "Not Charging")
        return round(BatteryStatus.__get_voltage(), 2)

    @staticmethod
    def __calculate_percentage_charge(voltage):
        # these are our reference voltages for a full/empty battery, in volts
        full_battery_voltage = 4.2
        # the values could vary by battery size/manufacturer so you might need to adjust them
        empty_battery_voltage = 2.8
        percentage = 100 * ((voltage - empty_battery_voltage) /
                            (full_battery_voltage - empty_battery_voltage))
        if percentage > 100:
            percentage = 100.00

        return percentage

    """
    Getting the battery percentage only works when the battery is not charging.
    This is because it utilises the voltage pin, that will display the usb voltage when charging.
    """
    @staticmethod
    def get_battery_percentage():
        if BatteryStatus.is_charging():
            raise IncorrectStateError("Charging", "Not Charging")
        # convert the raw ADC read into a voltage, and then a percentage
        voltage = BatteryStatus.__get_voltage()
        percentage = BatteryStatus.__calculate_percentage_charge(voltage)
        if percentage > 100:
            percentage = 100.00

        if (percentage < 0 and not BatteryStatus.is_charging()):
            raise LowVoltageError(voltage)

        return round(percentage)

    @staticmethod
    def is_charging():
        # Note - For non-wireless Pico, use Pin(24) instead of Pin('WL_GPIO2')
        charging_pin = Pin('WL_GPIO2', Pin.IN)
        return charging_pin.value() == 1

    @staticmethod
    def is_on_battery():
        return not BatteryStatus.is_charging()
