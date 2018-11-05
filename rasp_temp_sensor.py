"""
Script to log rasppi cpu temp
"""

import os
import datetime
import itertools
import time


def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    res = res.replace("temp=", "").replace("'C\n", "")
    return float(res)


class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        return get_cpu_temp()


sensor = Sensor()
timestamps = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
    print(stamp, value)
    time.sleep(1)

