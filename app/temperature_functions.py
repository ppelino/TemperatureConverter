#!/usr/bin/env python3
"""
created: 2022-03-10 19:02:45
@author: seraph★1001100
contact: seraph1001100@gmail.com
project: Temperature Converter
details: Converts Fahrenheit to Celsius and Celsius to Fahrenheit.
"""
import sys


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts fahrenheit to celsius.

    :param fahrenheit: temperature in fahrenheit.
    :return: temperature in celsius
    """

    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts celsius to fahrenheit.

    :param celsius: temperature in celsius.
    :return: temperature in fahrenheit
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def get_metric() -> [str, None]:
    """Allows users to select either fahrenheit, celsius or quit the program.

    :return: either fahrenheit, celsius or None
    """
    metric = ''
    while True:
        choice = input('Do you want to convert (f)ahrenheit, (c)elsius, or (q)uit?:\n> ')
        if choice not in 'fcq':
            print(error_message('Invalid Input! Enter either (f), (c) or (q)!'))
            continue
        else:
            break
    if choice == 'f':
        metric = 'fahrenheit'
    elif choice == 'c':
        metric = 'celsius'
    else:
        metric = None
    return metric


def error_message(s: str) -> str:
    """Changes text to red color. Used for errors."""
    return '\033[1;91m' + s + '\033[0m'


def output(s: str) -> str:
    """Returns the string output cyan"""
    return '\033[96m' + s + '\033[0m'


def is_valid(n: str) -> bool:
    """Tests if n is float or int"""
    try:
        float(n) or int(n)
        return True
    except ValueError:
        return False


def get_temperature(metric) -> float:
    """Asks for and returns temperature input"""
    while True:
        temperature = input(f'Enter the temperature in {metric}:\n> ')
        if not is_valid(temperature):
            print(error_message('Invalid input! Integer or float input only.'))
            continue
        else:
            break
    return float(temperature)


def calculate_temperature() -> None:
    """Main function of program. Calculates temperature conversion."""
    while True:
        metric = get_metric()
        if metric is None:
            print('Goodbye!')
            sys.exit()
        temperature = get_temperature(metric)
        if metric == 'fahrenheit':
            print(output(f'{temperature}° {metric} == {fahrenheit_to_celsius(temperature)}° celsius'))
        elif metric == 'celsius':
            print(output(f'{temperature}° {metric} == {celsius_to_fahrenheit(temperature)}° fahrenheit'))
        print()
