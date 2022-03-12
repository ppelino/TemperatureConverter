#!/usr/bin/env python3
"""
created: 2022-03-10 21:33:38
@author: seraph★1001100
contact: seraph1001100@gmail.com
project: Temperature Converter
"""

from app.temperature_functions import calculate_temperature


def main():
    print('This program converts fahrenheit to celsius, and celsius to fahrenheit.')
    calculate_temperature()


if __name__ == '__main__':
    main()
