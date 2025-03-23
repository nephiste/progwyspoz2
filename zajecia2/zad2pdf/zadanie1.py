# Tworzenie własnych wyjątków
class UserNotFoundError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserAuth:
    def __init__(self, users):
        self.users = users  # Inicjalizacja zewnętrznego słownika użytkowników

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(f"Użytkownik {username} nie został znaleziony w systemie.")

        if self.users[username] != password:
            raise WrongPasswordError("Nieprawidłowe hasło.")

        return f"Zalogowano {username}"


# Testowanie

auth = UserAuth({"admin": "1234", "user": "abcd"})  # Słownik przekazywany do konstruktora


test_data = [
    ("admin", "1234"),     # Poprawne dane
    ("unknown", "pass"),   # Nieznany użytkownik
    ("user", "wrongpass")  # Złe hasło
]

# Iteracja po testowych danych
for username, password in test_data:
    try:
        print(auth.login(username, password))
    except (UserNotFoundError, WrongPasswordError) as e:
        # Niezależnie od typu wyjątku, wypisujemy błąd
        print(f"Błąd: {e}")
