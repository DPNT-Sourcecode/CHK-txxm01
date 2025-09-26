
class HelloSolution:

    # friend_name = unicode string
    def hello(self, friend_name: str) -> str:
        if not isinstance(friend_name, str):
            raise TypeError("Expected argument to be a string")

        return f"Hello {friend_name}"
