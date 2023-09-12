#!/usr/bin/python3
"""
Prime number Game module.
"""


def isWinner(x, nums):
    """Prime number Game."""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve = [i for i in range(n + 1) if sieve[i]]
    c = 0
    for n in nums:
        for i in range(len(sieve)):
            if sieve[i] > n:
                break
            if sieve[i] <= n and (i + 1 == len(sieve) or sieve[i + 1] > n):
                c += 1
                break
    return "Ben" if c >= len(nums) / 2 else "Maria"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
