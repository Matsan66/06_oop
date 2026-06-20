from product import Product
from shopping_cart import ShoppingCart
from order import Order

class Webshop():
    """
    Webshop class represents a webshop
    """
    def __init__(self):

        # Create a products list for the webshop


        self.__products = [
            Product("Skruvmejsel Phillips PH2", 79.0),
            Product("Hammare 450 g", 149.0),
            Product("Polygriptång 250 mm", 199.0),
            Product("Måttband 5 m", 89.0),
            Product("Vattenpass 60 cm", 129.0),
            Product("Borrsats HSS 1–10 mm (19 delar)", 249.0),
            Product("Skiftnyckel 200 mm", 119.0),
            Product("Kombinationsnyckelset 8–19 mm", 399.0),
            Product("Batteridriven skruvdragare 18 V", 999.0),
            Product("Verktygslåda med 50 delar", 699.0),
        ]

        self.__shopping_cart = ShoppingCart()
        self.__orders = []

    # -------------------------------------------------------------

    # Property to get the shopping cart
    @property
    def shopping_cart(self):
        return self.__shopping_cart

    # Property to get orders
    @property
    def orders(self):
        return self.__orders

    # -------------------------------------------------------------

    def add_product(self, product_name, product_price):
        """
        Add a product to the webshop products list
        """
        self.__products.append(Product(product_name, product_price))

    # -------------------------------------------------------------

    def get_product_from_id(self, product_id):
        """
        Fetch a product from the webshop products list using product Id
        """
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    # -------------------------------------------------------------

    def present_products_table(self):
        """
        Present the webshop products list in a table
        """
        print(f"\n{'ID':<6} {'Namn':<40} {'Pris':>6}")
        print("-" * 60)

        for product in self.__products:
            print(f"{product.product_id:<6} {product.product_name:<40} {product.product_price:>6} kr")

    # -------------------------------------------------------------

    def add_order(self, order):
        """
        Add a submitted order to the orders list
        """
        self.__orders.append(order)
        print("Din order är skickad....")

    # -------------------------------------------------------------

    def present_orders(self):
        """
        Presents the webshop orders
        """
        if not self.__orders:
            print("Inga ordrar finns.")
            return

        for order in self.__orders:
            print(order)
            print()

 # -------------------------------------------------------------

def main():
    webshop = Webshop()

    webshop_menu = ["Visa menyn", "Visa produktlista", "Lägg till produkt", "Lägg vara i kundkorgen", "Ta bort vara ur kundkorgen", "Visa kundkorgen", "Skicka beställning", "Visa lagda order", "Avsluta"]

    for i in range(len(webshop_menu)):
        print(f"{i + 1:<4} {webshop_menu[i]:<40}")

    while True:

        # Loop to let user make a selection from the menu
        while True:

            try:
                menu_selection = int(input(f"\nVälj ett alternativ (1 - {len(webshop_menu)}): "))

                if 1 <= menu_selection <= len(webshop_menu):
                    break

                print(f"Fel: Du måste välja från menyn (1 - {len(webshop_menu)}).")

            except ValueError:
                print("Fel: Ange endast siffror.")

        # -------------------------------------------------------------

        # Menu chooice 1 : Display the webshop menu
        if menu_selection == 1:
            for i in range(len(webshop_menu)):
                print(f"{i + 1:<4} {webshop_menu[i]:<40}")

        # -------------------------------------------------------------

        # Menu chooice 2 : Display the webshop products list
        if menu_selection == 2:
            webshop.present_products_table()

        # -------------------------------------------------------------

        # Menu chooice 3 : Add a new product to webshop products list.
        elif menu_selection == 3:

            while True:
                try:
                    product_name = input(f"\nAnge att namn för den nya produkten: ")

                    if not product_name.strip():
                        raise ValueError("Produktens namn måste vara en ej tom sträng")

                    product_price = float(input("Ange produktens pris: "))

                    if product_price < 0:
                        raise ValueError("Produktens pris får inte vara negativt")

                    webshop.add_product(product_name, product_price)

                    print("Produkten har lagts till i produktlistan.")
                    break

                except ValueError as error:
                    print(f"Fel: {error}")

        # -------------------------------------------------------------

        # Menu chooice 4 : Add product to shopping cart by Id. Ask for number of items to add.
        elif menu_selection == 4:

            while True:
                try:
                    product_id = int(input(f"\nVälj en produkt att lägga i kundkorgen (produkt id): "))

                    product = webshop.get_product_from_id(product_id)

                    if product:
                        break

                    print("Fel: Produktens id finns inte i produktlistan")

                except ValueError:
                    print("Fel: Ange andast id från produktlistan.")

            while True:
                try:
                    product_amount = int(input(f"\nVälj antal av produkten att lägga i kundkorgen : "))

                    if product_amount > 0:
                        break

                    print("Fel: Antal produkter måste vara fler än noll.")

                except ValueError:
                    print("Fel: Ange ett heltal.")

            product = webshop.get_product_from_id(product_id)

            webshop.shopping_cart.add_product(product, product_amount)

        # -------------------------------------------------------------

        # Menu chooice 5 : Remove product to shopping cart by Id. Ask for number of items to remove.
        elif menu_selection == 5:

            while True:
                try:
                    product_id = int(input(f"\nVälj en produkt att ta bort ur varukorgen (produkt id): "))

                    product = webshop.get_product_from_id(product_id)

                    if product:
                        break

                    print("Fel: Produktens id finns inte i produktlistan")

                except ValueError:
                    print("Fel: Ange andast id från produktlistan.")

            while True:
                try:
                    product_amount = int(input(f"\nVälj antal av produkten att ta bort ur varukorgen: "))

                    if product_amount > 0:
                        break

                    print("Fel: Antal produkter måste vara fler än noll.")

                except ValueError:
                    print("Fel: Ange ett heltal.")

            if webshop.shopping_cart.remove_product(product_id, product_amount):
                print("Valda varor togs bort.")
            else:
                print("Varan finns inte i kundkorgen.")

        # -------------------------------------------------------------

        # Menu chooice 6 : Display the current shopping cart
        elif menu_selection == 6:
            print(webshop.shopping_cart)

        # -------------------------------------------------------------

        # Menu chooice 7 : Create an order from shopping cart content and clear the shopping cart.
        elif menu_selection == 7:
            order = Order(webshop.shopping_cart)
            webshop.add_order(order)
            webshop.shopping_cart.clear()

        # -------------------------------------------------------------

        # Menu chooice 8 : Display webshop orders history
        elif menu_selection == 8:
            webshop.present_orders()

        # -------------------------------------------------------------

        # Menu chooice 9 : Exit program loop and end program
        elif menu_selection == 9:
            print("\nTack för ditt besök. \nVälkommen åter.")
            break


if __name__ == "__main__":
    main()