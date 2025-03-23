from typing import Dict

class Library:
    def __init__(self) -> None:
        # Słownik przechowujący ISBN jako klucz i tytuł książki jako wartość
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        """Dodaje książkę do biblioteki"""
        self.books[isbn] = title

    def find_book(self, isbn: str) -> str:
        """Znajduje książkę po numerze ISBN i zwraca tytuł lub None, jeśli książki nie ma"""
        return self.books.get(isbn, None)

# Przykład użycia:
library = Library()
library.add_book("978-3-16-148410-0", "Python dla każdego")
library.add_book("978-0-07-180855-8", "Człowiek w poszukiwaniu sensu")

# Wyszukiwanie książki
print(library.find_book("978-3-16-148410-0"))  # Python dla każdego
print(library.find_book("978-1-23-456789-0"))  # None
