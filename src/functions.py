import re

def separate_name(name):
    # splits name by putting a space before every uppercased letter
    v = re.split("([A-Z])", name)[1:]
    e, r = v[::2], v[1::2]
    return " ".join((e[i] + r[i] for i in range(len(e))))
