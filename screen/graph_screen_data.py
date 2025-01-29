from libs.battery import BatteryStatus
from libs.wifi import Wifi
import urequests
import machine


class GraphScreenData():

    @staticmethod
    def get_time_from_api():
        url = f"https://timeapi.io/api/time/current/zone?timeZone=Europe%2FLondon"
        headers = {
            'Accept': 'application/json',
        }
        Wifi.connect()
        response = urequests.get(url, headers=headers)
        Wifi.disconnect()
        data = response.json()
        return data

    @staticmethod
    def set_time(new_time):
        rtc = machine.RTC()
        print('Setting time')
        print(new_time)
        # (year, month, day, weekday, hours, minutes, seconds, subseconds)
        rtc.datetime((new_time["year"], new_time["month"],
                      new_time["day"], 0, new_time["hour"], new_time["minute"], new_time["seconds"], 0))
        print('time set')

    @staticmethod
    def get_time():
        rtc = machine.RTC()
        dt = rtc.datetime()
        formatted_time = f"{dt[0]:04}-{dt[1]:02}-{dt[2]
            :02} | {dt[4]:02}:{dt[5]:02}:{dt[6]:02}"
        return formatted_time

    @staticmethod
    def get_battery_data():

        is_on_battery = BatteryStatus.is_on_battery()
        battery_percentage = f'{
            BatteryStatus.get_battery_percentage()}%' if is_on_battery else 'N/A%'
        voltage = f'{BatteryStatus.get_voltage(
        )}' if is_on_battery else 'N/A V'
        return {
            "is_on_battery": is_on_battery,
            "battery_percentage": battery_percentage,
            "voltage": voltage
        }

    @staticmethod
    def get_data():
        battery_data = GraphScreenData.get_battery_data()
        return battery_data
