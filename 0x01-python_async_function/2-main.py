#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9
print(
    f"Approximate elapsed time falls within an acceptable range: {0 <= measure_time(n, max_delay) <= max_delay * 1.02}."
)
print(measure_time(n, max_delay))
