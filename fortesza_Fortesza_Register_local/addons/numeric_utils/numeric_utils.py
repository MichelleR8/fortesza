from .actions import FilterDigits


class NumericUtils:
    @staticmethod
    def filterdigits(input: str) -> FilterDigits:
        """Remove all non numeric characters from {{input}}."""
        return FilterDigits(input)
