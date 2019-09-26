import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import common_util


def lm317_vout(r1, r2):
    if common_util.is_float_number(r1):
        r1 = float(r1)
    else:
        r1 = common_util.decode_resistor_value(r1)

    if common_util.is_float_number(r2):
        r2 = float(r2)
    else:
        r2 = common_util.decode_resistor_value(r2)

    print(str(1.25 * (1 + (r2/r1))) + "V")


