# si_formatter

si_prefix = {
    0: '',
    1: 'k',  # kilo
    2: 'M',  # Mega
    3: 'G',  # Giga
    4: 'T',  # Tera
    5: 'P',  # Peta
    6: 'E',  # Exa
    7: 'Z',  # Zeta
    8: 'Y'   # Yotta
}


def return_with_si(value, unit):
    prefix = 0
    if prefix < si_prefix.keys().__len__():
        while value >= 1e3:
            value /= 1e3
            prefix += 1

    # if >= one million grams convert units to tons
    if unit == 'g' and prefix >= 2:
        unit = 'ton(s)'
        prefix -= 2

    return "%.2f %s%s" % (value, si_prefix[prefix], unit)
