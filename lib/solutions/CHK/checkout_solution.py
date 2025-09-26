
class CheckoutSolution:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
        self.multi_offers = {
        "A": [(5, 200), (3, 130)], # (quantity, offer price)
        "B": [(2, 45)],
            # C, D, E have no multi-pack price (E has a cross-item freebie instead)
        }

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        # Prices and special offers
        # prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        # special_offers = {
        #     "A": (3, 130), # (quantity, offer price)
        #     "B": (2, 45),
        # }
        # multi_offers = {
        # "A": [(5, 200), (3, 130)], # (quantity, offer price)
        # "B": [(2, 45)],
        #     # C, D, E have no multi-pack price (E has a cross-item freebie instead)
        # }

        # Validate input
        if not isinstance(skus, str):
            return -1

        # Count items in skus
        counts = {}
        for sku in skus:
            sku = sku.strip()
            # ignore empty strings
            if not sku:
                continue

            if sku not in self.prices:
                return -1

            counts[sku] = counts.get(sku, 0) + 1

        print('counts: ', counts)
        print()

        # Handle special offer for E: for every 2 E purchased, one B is free
        effective_b_to_charge = 0
        if counts.get("E", 0) > 0 and counts.get("B", 0) > 0:
            free_b = counts.get("E", 0) // 2
            print('free b: ', free_b)
            print()
            # You cannot get more free B than you actually have in the basket
            effective_b_to_charge = max(0, counts.get("B", 0) - free_b)
        else:
            effective_b_to_charge = counts.get("B", 0)

        print('effective_b_to_charge: ', effective_b_to_charge)

        total = 0
        # Apply special offers
        for item, qty in counts.items():
            # if item not in special_offers:
            #     total += qty * prices[item]
            #     continue

            # offer_qty, offer_price = special_offers[item]
            # Check how many offers apply
            # num_offers, remainder = divmod(qty, offer_qty)
            # total += num_offers * offer_price + remainder * prices[item]

            if item in ["B"] and effective_b_to_charge:
                qty = effective_b_to_charge
            print('item: ', item, 'qty: ', qty)
            print()

            total += self.price_with_offers(item, qty)

        return total

    def price_with_offers(self, sku: str, qty: int) -> int:
        # Price qty units of sku applying multi-pack offers to benefit customer
        # (largest pack first). Falls back to unit price for remainder.
        if qty <= 0:
            return 0

        total = 0
        packs = self.multi_offers.get(sku, [])
        # Make sure largest-first
        packs = sorted(packs, key=lambda x: x[0], reverse=True)
        remaining = qty
        for pack_qty, pack_price in packs:
            if pack_qty <= 0:
                continue
            n_packs, remaining = divmod(remaining, pack_qty)
            if n_packs:
                total += n_packs * pack_price

        total += remaining * self.prices[sku]

        return total




