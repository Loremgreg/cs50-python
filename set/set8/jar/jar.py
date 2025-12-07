class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
          return self.size * "🍪"
        # return n (number of cookies in the cookie jar)

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n
        return f"Deposit: {n} cookies"

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        self._size -= n

        return f"Withdraw: {n} cookies"

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


cookies = Jar()
cookies.deposit(10)
cookies.withdraw(4)
print(cookies)

