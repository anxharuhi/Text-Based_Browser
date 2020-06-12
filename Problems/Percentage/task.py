def get_percentage(number, round_digits=0):
    return str(round(number * 100, round_digits if round_digits else None)) + '%'
