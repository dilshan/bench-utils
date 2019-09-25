from IPython.display import HTML, display
import tabulate
import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import common_util

res24_set1 = [0.1, 0.11, 0.12, 0.13, 0.15, 0.16, 0.18, 0.2, 0.22, 0.24, 0.27, 0.3, 0.33, 0.36, 0.39, 0.43, 0.47, 0.51,
              0.56, 0.62, 0.68, 0.75, 0.82, 0.91, 1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3,
              3.6, 3.9, 4.3, 4.7, 5.1, 0.6, 6.2, 6.8, 7.5, 8.2, 9.1, 10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30,
              33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]

res24_set2 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8,
              7.5, 8.2, 9.1]

res_multiplier = [1, 10, 100, 1000, 10000, 100000, 1000000]


def basic_voltage_div(vcc, r1, r2):
    if common_util.is_float_number(r1):
        r1 = float(r1)
    else:
        r1 = common_util.decode_resistor_value(r1)

    if common_util.is_float_number(r2):
        r2 = float(r2)
    else:
        r2 = common_util.decode_resistor_value(r2)

    print(str((vcc * r2) / (r1 + r2)) + "V")

# ----------------------------------------------------------------------------------------------------------------------


def find_voltage_div_resistors(vcc, out):
    ratio = out / vcc
    min_diff = 1

    output_table = []

    if ratio == 0.5:
        print("R1 = R2")
        return

    if vcc / out >= 93.0:
        print("Voltage ratio is high")
        return

    if vcc / out <= 1.009:
        print("Voltage ratio is low")
        return

    for res1 in res24_set1:
        for res2 in res24_set2:
            check_ratio = res2 / (res1 + res2)
            diff = abs(ratio - check_ratio)
            if diff <= min_diff:
                min_diff = diff

    for res1 in res24_set1:
        for res2 in res24_set2:
            check_ratio = res2 / (res1 + res2)
            diff = abs(ratio - check_ratio)
            if diff == min_diff:
                for factor in res_multiplier:
                    data_entry = [common_util.format_resistor_value(factor * res1), common_util.format_resistor_value(factor * res2)]
                    output_table.append(data_entry)

                display(HTML(tabulate.tabulate(output_table, tablefmt='html', headers=["R1", "R2"])))
                output_table = []
