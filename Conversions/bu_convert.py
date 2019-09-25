import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import common_util

def to_binary(number, output_length=8):
    if output_length < 8:
        print("Invalid length. Minimum allowed length is 8.")
        return

    format_specifier = "{0:0" + str(output_length) + "b}"
    binary_str = format_specifier.format(number)

    # Forcefully format output into 8 (char) blocks if converted string is not fit into 8 (char) blocks.
    if (len(binary_str) % 8) != 0:
        output_length = ((len(binary_str) // 8) + 1) * 8

        format_specifier = "{0:0" + str(output_length) + "b}"
        binary_str = format_specifier.format(number)

    if len(binary_str) > 8:
        output_block = [binary_str[pos:pos + 8] for pos in range(0, len(binary_str), 8)]

        for block_data in output_block:
            print(block_data, end=" ")

        print()
    else:
        print(binary_str)

# ----------------------------------------------------------------------------------------------------------------------


def to_hex(number, output_length=2):
    if output_length < 2:
        print("Invalid length. Minimum allowed length is 2.")
        return

    output_formatter = "0x%0." + str(output_length) + "X"
    print(output_formatter % number)

# ----------------------------------------------------------------------------------------------------------------------


def to_frequency(time_value):
    time_value = str(time_value).lower()
    unit = 1
    strip_length = -1

    if 'ps' in time_value:
        unit = 1e-12
        strip_length = -2
    elif 'ns' in time_value:
        unit = 1e-9
        strip_length = -2
    elif 'us' in time_value:
        unit = 1e-6
        strip_length = -2
    elif 'ms' in time_value:
        unit = 1e-3
        strip_length = -2

    time_value = float(time_value[0:strip_length])
    freq = 1 / (time_value * unit)

    print(common_util.format_freq_value_ex(freq))

# ----------------------------------------------------------------------------------------------------------------------


def to_period(freq_value):
    freq_value = str(freq_value).lower()
    unit = 1
    strip_length = -2

    if 'ghz' in freq_value:
        unit = 1e+9
        strip_length = -3
    elif 'mhz' in freq_value:
        unit = 1e+6
        strip_length = -3
    elif 'khz' in freq_value:
        unit = 1e+3
        strip_length = -3

    freq_value = float(freq_value[0:strip_length])
    time_val = 1 / (freq_value * unit)

    print(common_util.format_time_value_ex(time_val))

# ----------------------------------------------------------------------------------------------------------------------


def hex_to_bcd(in_number):
    print(''.join(format(int(c), '04b') for c in str(int(in_number, 16))))

# ----------------------------------------------------------------------------------------------------------------------


def int_to_bcd(in_number):
    print(''.join(format(int(c), '04b') for c in str(int(in_number))))

# ----------------------------------------------------------------------------------------------------------------------
