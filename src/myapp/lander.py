# 2 Länder

"""
1a På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt
för länderna. (Data från januari 2024. Avrunda befolkningen.)
"""

class Country:
    """
    Represents a country by name, population, area and languages
    Languages can be added with add_language().
    Country information can be viewed with print_info().
    """
    def __init__(self, name, pop, area = None):
        """
        Creates a country with namn, population, area and languages list
        :param name (str): Country namn
        :param pop (int/ float): Country population
        :param area(int, float eller None): Country area
        :param languages(list): Initially empty languages list
        """
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = []

    def print_info(self):
        """
        Prints the country information
        """

        print(F"\nI {self.__name} bor det {self.__population} miljoner invånare.", end = "")
        if self.__area:
            print(f" Arean är {self.__area}")
        else:
            print()

        for language in self.__languages:
            print(f"{language} ", end = "")
        print("")

    def add_language(self, language):
        """
        Adds a languages to the countrys language list
        :param language: Language to be added
        """
        self.__languages.append(language)

def main():
    """
    Demonstrates usage of the Country class by:
    - creating Country objects
    - adding country languages
    - printing country information
    """

    # Skapa landobjekt med namn, population och area
    se = Country("Sverige", 10.5)
    no = Country("Norge", 5.5)
    fi = Country("Finland", 5.6, 338440)
    ch = Country("Schweiz", 9, 41290)

    # Lägg till landets officiella språk
    se.add_language("Svenska")
    no.add_language("Norska")
    fi.add_language("Svenska, Finska")
    fi.add_language("Finska")
    ch.add_language("Tyska")
    ch.add_language("Franska")
    ch.add_language("Italienska")
    ch.add_language("Rätoromanska")

    # Skriv ut ländernas information
    se.print_info()
    no.print_info()
    fi.print_info()
    ch.print_info()


if __name__ == "__main__":
    main()