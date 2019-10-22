class RecurFibo:

    @staticmethod
    def recur_fibo(n):
        """Recursive function to
        print Fibonacci sequence"""
        if n <= 1:
            return n
        else:
            return RecurFibo.recur_fibo(n - 1) + RecurFibo.recur_fibo(n - 2)


