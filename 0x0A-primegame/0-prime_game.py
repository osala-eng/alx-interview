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

    # Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    prime_numbers = [i for i, is_prime in enumerate(sieve) if is_prime]

    c = 0
    num_primes = len(prime_numbers)

    # Binary search function to find the index of the first prime >= n
    def binary_search(nums, n):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= n:
                right = mid - 1
            else:
                left = mid + 1
        return left

    for num in nums:
        index = binary_search(prime_numbers, num)
        if index < num_primes and prime_numbers[index] == num:
            c += 1

    return "Ben" if c >= len(nums) / 2 else "Maria"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
