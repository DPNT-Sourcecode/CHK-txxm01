
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        # Prices and special offers
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        special_offers = {
            "A": (3, 130), # (quantity, offer price)
            "B": (2, 45),
        }

        # Validate input
        if not isinstance(skus, str):
            return -1

        # for sku in skus:
        #     if sku not in prices:
        #         print('sku: ', sku)
        #         print()

        # validate = [sku.strip() for sku in skus if sku.strip() not in prices and sku.strip() != ""]
        # print('validate: ', validate)

        # if len(validate) > 0:
        #     print('fail')
        #     return -1

        # Count items in skus
        counts = {}
        for sku in skus:
            sku = sku.strip()
            # ignore empty strings
            if not sku:
                continue

            if sku not in prices:
                return -1

            counts[sku] = counts.get(sku, 0) + 1

        total = 0
        # Apply special offers
        for item, qty in counts.items():
            if item not in special_offers:
                total += qty * prices[item]
                continue

            offer_qty, offer_price = special_offers[item]
            # Check how many offers apply
            num_offers, remainder = divmod(qty, offer_qty)
            total += num_offers * offer_price + remainder * prices[item]

        return total
