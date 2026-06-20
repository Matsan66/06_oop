class Order():
    """
    Class to represent a webshop order
    """

    next_order_id = 1000

    def __init__(self, shopping_cart):

        self.__order_id = Order.next_order_id
        self.__order = shopping_cart
        Order.next_order_id += 1

        self.__items = shopping_cart.shopping_cart.copy()
        self.__order_sum = shopping_cart.shopping_cart_sum()


    # Get the order ID
    @property
    def order_id(self):
        return self.__order_id

    # Get the order
    @property
    def order(self):
        return self.__order

    # Get the sum
    @property
    def order_sum(self):
        return self.__order_sum

    # Returns a string representation of the order
    def __str__(self):
        rows = "\n".join(
            f"{product.product_name:<35} {amount:>5} "
            f"{product.product_price * amount:>8} kr"
            for product, amount in self.__items
        )

        return (
            f"\nORDER #{self.__order_id}\n"
            f"{'-' * 60}\n"
            f"{rows}\n"
            f"{'-' * 60}\n"
            f"Totalt: {self.__order_sum} kr"
        )