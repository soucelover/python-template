def fibonacci(index: int) -> int:
    """Get number from Fibonacci sequence.

    0 1 1 2 3 5 8 13 21 34 55 89 144 . . .

    Args:
        index: Index of the number.

    Returns:
        Number from Fibonacci sequence.
    """
    if index in (0, 1):
        return index

    a = 0
    b = 1

    for _ in range(index - 1):
        a, b = b, a + b

    return b
