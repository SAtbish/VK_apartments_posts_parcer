import re

import numpy as np


def find_apartment_cost(string: str):
    patterns = [
        *[rf'\b\d+{char}{num}' for num in ["000", 500, 250, 750] for char in ["\.", "\s", ","]],
        *[rf"\b\d+{char}{word}\b" for word in [
            "тысяч", "тыс", "тыс.", "т", "т.", "k", "к", "₽", "руб", "руб.", "р", "р."
        ] for char in ["", "\s"]],
        r'\b\d{2}(?=-\d{2})',
        r'\b\d{4,5}\b'
    ]

    for pattern in patterns:
        match = re.search(pattern, string, flags=re.IGNORECASE)
        if match:
            number = int(re.findall(r'\d+', match.group())[0])
            return number * 1000 if number < 1000 else number

    return np.NaN
