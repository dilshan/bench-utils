def is_float_number(in_str):
    try:
        float(in_str)
        return True
    except ValueError:
        return False

# ----------------------------------------------------------------------------------------------------------------------


def decode_resistor_value(res_value):
    prefix_val = float(res_value[0:-1])
    res_suffix = str(res_value[-1]).upper()
    multiplier = 1

    if res_suffix == 'K':
        multiplier = 1000
    elif res_suffix == 'M':
        multiplier = 1000000

    return prefix_val * multiplier

# ----------------------------------------------------------------------------------------------------------------------


def strip_trail_zero(val):
    return ('%f' % val).rstrip('0').rstrip('.')

# ----------------------------------------------------------------------------------------------------------------------


def format_resistor_value(in_val):
    if in_val < 1000:
        return strip_trail_zero(in_val) + 'Ω'
    elif in_val < 1000000:
        return strip_trail_zero(in_val / 1000) + 'KΩ'
    else:
        return strip_trail_zero(in_val / 1000000) + 'MΩ'

# ----------------------------------------------------------------------------------------------------------------------


def format_freq_value(in_val):
    if in_val < 1e+3:
        return strip_trail_zero(in_val) + 'Hz'
    elif in_val < 1e+6:
        return strip_trail_zero(in_val / 1e+3) + 'KHz'
    elif in_val < 1e+9:
        return strip_trail_zero(in_val / 1e+6) + 'MHz'
    else:
        return strip_trail_zero(in_val / 1e+9) + 'GHz'

# ----------------------------------------------------------------------------------------------------------------------


def format_freq_value_ex(in_val):
    return strip_trail_zero(in_val) + "Hz\n" + strip_trail_zero(in_val / 1e+3) + "KHz\n" + \
           strip_trail_zero(in_val / 1e+6) + "MHz\n" + strip_trail_zero(in_val / 1e+9) + "GHz"

# ----------------------------------------------------------------------------------------------------------------------


def format_time_value(in_val):
    if in_val > 1e-3:
        return strip_trail_zero(in_val) + 's'
    elif in_val > 1e-6:
        return strip_trail_zero(in_val / 1e-3) + 'ms'
    elif in_val > 1e-9:
        return strip_trail_zero(in_val / 1e-6) + 'us'
    elif in_val > 1e-12:
        return strip_trail_zero(in_val / 1e-9) + 'ns'
    else:
        return strip_trail_zero(in_val / 1e-12) + 'ps'

# ----------------------------------------------------------------------------------------------------------------------


def format_time_value_ex(in_val):
    return strip_trail_zero(in_val) + "s\n" + strip_trail_zero(in_val / 1e-3) + "ms\n" + \
           strip_trail_zero(in_val / 1e-6) + "us\n" + strip_trail_zero(in_val / 1e-9) + "ns\n" + \
           strip_trail_zero(in_val / 1e-12) + "ps"

# ----------------------------------------------------------------------------------------------------------------------


def display_numeric_result(val):
    base10_result = str(val)
    base16_result = "0x%0.4X" % val
    base2_result = "{0:02b}".format(val)

    print("BASE 2 : " + base2_result)
    print("BASE 10 : " + base10_result)
    print("BASE 16 : " + base16_result)

# ----------------------------------------------------------------------------------------------------------------------
