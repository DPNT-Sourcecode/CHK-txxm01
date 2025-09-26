
class CheckoutSolution:
    def __init__(self):
        # Unit prices
        self.prices = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
            "G": 20, "H": 10, "I": 35, "J": 60, "K": 70, "L": 90,
            "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
            "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17,
            "Y": 20, "Z": 21,
        }
        # Multi-pack offers (largest-first will be enforced at runtime)
        # Each entry is list of tuples: (pack_qty, pack_price)
        self.multi_offers = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "H": [(10, 80), (5, 45)],
            "K": [(2, 120)],        # updated
            "P": [(5, 200)],
            "Q": [(3, 80)],
            "V": [(3, 130), (2, 90)],
        }
        # Self-freebies: for each group size, 1 free within the group
        # .e.g. F: 2F get 1F free => every 3 F, 1 is free
        self.self_free_group: dict[str, int] = {
            "F": 3,
            "U": 4,
        }
        # Cross-item freebies: trigger_sku -> (target_sku, trigger_qty_for_one_free_target)
        # .e.g. E: every 2 E gives 1 B free
        self.cross_free: dict[str, tuple[str, int]] = {
            "E": ("B", 2),
            "N": ("M", 3),
            "R": ("Q", 3),
        }
        # -------- Group discount offer --------
        # .e.g. "Buy any 3 of (S,T,X,Y,Z) for 45"
        self.group_offer_items = ("S", "T", "X", "Y", "Z")
        self.group_offer_size = 3
        self.group_offer_price = 45

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

        chargeable = self.chargeable_quantities(counts)

        # Applu group discounts
        # bundle_total, chargeable = self.price_group_bundles(chargeable)
        price_list = []
        for sku in self.group_offer_items:
            qty = chargeable.get(sku, 0)

            if qty <= 0:
                continue

            price_list.append(self.prices[sku] * qty)
            chargeable[sku] = 0

        if not price_list:
            return 0

        bundle_count = len(price_list) // self.group_offer_size

        price_list.sort(reverse=True)
        # Sum of bundled items
        # bundle_prices = price_list[:bundle_count * self.group_offer_size]
        remaining_prices = price_list[bundle_count * self.group_offer_size:]

        total = bundle_count * self.group_offer_price + sum(remaining_prices)

        # total = 0
        # Apply special offers
        for item, qty in chargeable.items():
            if qty <= 0:
                continue

            total += self.price_with_offers(item, qty)

        return total

    def chargeable_quantities(self, counts: dict):
        """Determine chargeable quantities"""
        chargeable = counts
        # Apply freebies
        for sku, group in self.self_free_group.items():
            qty = counts.get(sku, 0)
            if qty > 0 and group > 1:
                free_units = qty // group  # 1 free per full group
                chargeable[sku] = max(0, qty - free_units)

        # Apply cross-item freebies
        for trigger, (target, trigger_qty) in self.cross_free.items():
            tqty = counts.get(trigger, 0)
            tgt_qty = chargeable.get(target, 0)
            if tqty > 0 and tgt_qty > 0 and trigger_qty > 0:
                free_units = tqty // trigger_qty
                chargeable[target] = max(0, tgt_qty - free_units)

        return chargeable

    def price_group_bundles(self, chargeable: dict) -> tuple[int, dict]:
        """Apply group bundles"""
        # Flast price list for group items
        price_list = []
        for sku in self.group_offer_items:
            qty = chargeable.get(sku, 0)

            if qty <= 0:
                continue

            price_list.append(self.prices[sku] * qty)

        if not price_list:
            return 0

        bundle_count = len(price_list) // self.group_offer_size

        price_list.sort(reverse=True)
        # Sum of bundled items
        bundle_prices = price_list[:bundle_count * self.group_offer_size]
        remaining_prices = price_list[bundle_count * self.group_offer_size:]
        total = bundle_count * self.group_offer_price + sum(remaining_prices)

        for sku in self.group_offer_items:
            chargeable[sku] = 0

        return total, chargeable



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


