class CountdownTimer:
    def start(self, n):
        """Counts down from n to 0 and returns the sequence as a list."""
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("Input must be an integer")
        if n > 10000000:
            raise ValueError("Input too large to process")
        if n <= 0:
            raise ValueError("Input must be a positive integer")
        return list(range(n, -1, -1))
    

