import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import common_util

eia_96_code = [100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162,
               165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267,
               274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442,
               453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732,
               750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976]

eia_96_suffix = {
    "Z": 0.001,
    "Y": 0.01,
    "R": 0.01,
    "X": 0.1,
    "S": 0.1,
    "A": 1,
    "B": 10,
    "H": 10,
    "C": 100,
    "D": 1000,
    "E": 10000,
    "F": 100000
}


def smd_resistor(input_code):
    resistor_value = -1

    if len(input_code) == 3:
        if input_code.isdigit():
            resistor_value = float(input_code[0:2]) * (10 ** int(input_code[2]))
        elif 'R' in input_code:
            resistor_value = float(input_code.replace('R', '.'))
        elif input_code[0:2].isdigit():
            resistor_value = eia_96_code[int(input_code[0:2]) - 1] * eia_96_suffix[input_code[2]]
    elif len(input_code) == 4:
        if 'R' in input_code:
            resistor_value = float(input_code.replace('R', '.'))
        else:
            resistor_value = float(input_code[0:3].replace('R', '.')) * (10 ** int(input_code[3]))

    if resistor_value >= 0:
        print(common_util.format_resistor_value(resistor_value))
    else:
        print("Invalid resistor value!")
