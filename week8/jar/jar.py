class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self.max_capacity = capacity
        self.nb_cookie = 0

    def __str__(self):
        return str("🍪" * self.nb_cookie)

    def deposit(self, n):
        if not isinstance(n, int) or n < 0 or (n + self.nb_cookie) > self.max_capacity:
            raise ValueError
        self.nb_cookie += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0 or n > self.nb_cookie:
            raise ValueError
        self.nb_cookie -= n

    @property
    def capacity(self):
        return self.max_capacity

    @property
    def size(self):
        return self.nb_cookie
