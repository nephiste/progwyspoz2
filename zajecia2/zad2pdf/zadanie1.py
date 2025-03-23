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

# Test przypadków
try:
    print(auth.login("admin", "1234"))  # Powinno zalogować
except UserNotFoundError as e:
    print(e)
except WrongPasswordError as e:
    print(e)

try:
    print(auth.login("unknown", "pass"))  # Powinno rzucić UserNotFoundError
except UserNotFoundError as e:
    print(f"Błąd: {e}")
except WrongPasswordError as e:
    print(e)

try:
    print(auth.login("user", "wrongpass"))  # Powinno rzucić WrongPasswordError
except UserNotFoundError as e:
    print(e)
except WrongPasswordError as e:
    print(f"Błąd: {e}")
