n = float(input())


def MinDivisor(n):
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        else:
            return n


print(int(MinDivisor(n)))
