
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus) -> int:
        # Prices and special offers
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        special_offers = {
            "A": (3, 130), # (quantity, offer price)
            "B": (2, 45),
        }
