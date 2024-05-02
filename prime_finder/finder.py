def find_primes(up_to: int | float) -> list[int | float]:
    primes = []
    if up_to < 0:
        raise ValueError("'up_to' must be greater than 0")
    if up_to == 0 or up_to == 1:
        return primes
    elif up_to == 2:
        primes.append(2)
        return primes
    else:
        for value in range(2, up_to):
            if value == 2:
                primes.append(2)
            else:
                for prev in primes:
                    if value % prev == 0:
                        break
                else: primes.append(value)
    return primes