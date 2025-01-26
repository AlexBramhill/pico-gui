from machine import ADC, Pin
from errors import LowVoltageError

"""
Modified version of the battery_pico.py file from
https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_lipo_shim/battery_pico.py.
"""


class BatteryStatus:
    __vsys = ADC(Pin(29))                 # reads the system input voltage

    # reading GP24 tells us whether or not USB power is connected
    __charging = Pin(24, Pin.IN)
    __conversion_factor = 3 * 3.3 / 65535

    # these are our reference voltages for a full/empty battery, in volts
    __full_battery_voltage = 4.2
    # the values could vary by battery size/manufacturer so you might need to adjust them
    __empty_battery_voltage = 2.8

    @staticmethod
    def get_battery_percentage():
        # convert the raw ADC read into a voltage, and then a percentage
        voltage = BatteryStatus.__vsys.read_u16() * BatteryStatus.__conversion_factor
        percentage = 100 * ((voltage - BatteryStatus.__empty_battery_voltage) /
                            (BatteryStatus.__full_battery_voltage - BatteryStatus.__empty_battery_voltage))
        if percentage > 100:
            percentage = 100.00

        if (percentage < 0 and not BatteryStatus.is_charging()):
            raise LowVoltageError(voltage)

        return percentage

    @staticmethod
    def is_charging():
        return BatteryStatus.__charging.value() == 1
