def middle_square(num: int, a: float = 0, b: float = 1) -> float:
    return a + int(str(num**2)[-6:-2]) / (b - a)
