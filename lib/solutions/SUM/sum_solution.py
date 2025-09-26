
class SumSolution:
    def compute(self, x: int, y: int):
        if not (isinstance(x, int) or isinstance(y, int)):
            raise TypeError("Expected both arguments to be integers!")

        return x + y
