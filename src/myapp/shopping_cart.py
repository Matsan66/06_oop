class ShoppingCart():
    """
    Class represents a webshop shopping cart
    """

    next_shopping_cart_id = 1000

    # Create a shopping cart with ID and an empty cart
    def __init__(self):
        self.__shopping_cart_id = ShoppingCart.next_shopping_cart_id
        self.__shopping_cart  = []
        ShoppingCart.next_shopping_cart_id += 1

    # Get the cart ID
    @property
    def id(self):
        return self.__shopping_cart_id

    # Get the shopping cart
    @property
    def shopping_cart(self):
        return self.__shopping_cart

    # Add a product from webshop product list to shopping cart
    def add_product(self, product, amount):

        if product is None:
            raise ValueError(f"Fel: Kunde inte hitta produkten")
        self.__shopping_cart.append((product, amount))


    # Remove a product or items from the shopping cart
    def remove_product(self, product_id, amount):

        for product, quantity in self.__shopping_cart:

            if product.product_id == product_id:

                if amount >= quantity:
                    self.__shopping_cart.remove((product, quantity)) # Remove entire product
                else:
                    index = self.__shopping_cart.index((product, quantity)) # Remove items from product
                    self.__shopping_cart[index] = (
                        product,
                        quantity - amount
                    )

                return True

        return False

    def shopping_cart_sum(self):
        total = sum(
            product.product_price * amount
            for product, amount in self.__shopping_cart
        )
        return total

    def clear(self):
        self.__shopping_cart.clear()

    # Returns a string representation of the shoppingcart

    def __str__(self):
        banner = "VARUKORG"
        header = f"{'ID':<6} {'Produkt':<35} {'Antal':>5} {'Summa':>10}"
        line = "-" * 65

        rows = "\n".join(
            f"{product.product_id:<6} "
            f"{product.product_name:<35} "
            f"{amount:>5} "
            f"{product.product_price * amount:>8} kr"
            for product, amount in self.__shopping_cart
        )

        total_sum = f"Total: {self.shopping_cart_sum():>4} kr"

        return f"\n{banner}\n{line}\n{header}\n{line}\n{rows}\n{line}\n{total_sum}"



