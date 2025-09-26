
class SumSolution:
    def compute(self, x: int, y: int) -> int:
        if not (isinstance(x, int) or isinstance(y, int)):
            raise TypeError("Expected both arguments to be integers")

        if any([
            x < 0,
            x > 100,
            y < 0,
            y > 100,
        ]):
            raise ValueError("Arguments must be between 0 and 100")

        return x + y


