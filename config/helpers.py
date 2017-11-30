from typing import List


def array_indented(level: int, l: List[str]) -> str:
    out = "[\n"
    for x in l:
        out += (((level+1) * 4) * " ") + '"{}"'.format(x) + ",\n"
    out += ((level * 4) * " ") + "]"
    return out
