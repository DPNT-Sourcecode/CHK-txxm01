
class CheckoutSolution:
    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
        self.multi_offers = {
        "A": [(5, 200), (3, 130)], # (quantity, offer price)
        "B": [(2, 45)],
            # C, D, E have no multi-pack price (E has a cross-item freebie instead)
        }

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        """Process checkout of items in basket"""
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

        # Handle special offer for E: for every 2 E purchased, one B is free
        b_count = counts.get("B", 0)
        e_count = counts.get("E", 0)
        free_b = e_count // 2
        effective_b_to_charge = max(0, b_count - free_b)

        # Handle special offer for F: buy 2Fs and get another F free
        f_count = counts.get("F", 0)
        free_f = f_count // 3  # for each 3 F, 1 is free
        effective_f_to_charge = f_count - free_f

        total = 0
        # Apply special offers
        for item, qty in counts.items():
            if item in ["B"]:
                qty = effective_b_to_charge

            if item in ["F"]:
                qty = effective_f_to_charge

            total += self.price_with_offers(item, qty)

        return total

    def price_with_offers(self, sku: str, qty: int) -> int:
        """Price qty units of sku applying multi-pack offers to benefit customer
        (largest pack first). Falls back to unit price for remainder.
        """
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


