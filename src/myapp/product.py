class Product():
    """
    Class representing a product
    """

    next_product_id = 1001

    def __init__(self, product_name, product_price):
        self.__product_id = Product.next_product_id
        self.__product_name = product_name
        self.__product_price = product_price
        Product.next_product_id += 1

    # Properties and setters to access product object data

    # get product-id
    @property
    def product_id(self):
        return self.__product_id

    # get product_name
    @property
    def product_name(self):
        return self.__product_name

    # Set product_name
    @product_name.setter
    def product_name(self, new_name):
        if not new_name:
            raise ValueError("Namn får inte vara tomt")
        self.__product_name = new_name

    # get product_price
    @property
    def product_price(self):
        return self.__product_price

    # Set product_name
    @product_price.setter
    def product_price(self, new_price):
        if not new_price:
            raise ValueError("Pris får inte vara tomt")
        self.__product_price = new_price

    # Displays the product
    def __str__(self):
        return f"{self.__product_id} | {self.__product_name} | {self.__product_price} kr"
