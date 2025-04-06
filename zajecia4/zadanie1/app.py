from flask import Flask, render_template, abort

# Tworzenie aplikacji Flask
app = Flask(__name__)

# Przykładowe dane użytkowników
users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users_list():
    # Przekazuje listę użytkowników do szablonu
    return render_template('users.html', users=users)

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    # Sprawdza, czy użytkownik istnieje
    user = users.get(user_id)
    if user:
        return render_template('user_profile.html', user=user)
    else:
        return "Użytkownik nie istnieje", 404

if __name__ == '__main__':
    app.run(debug=True)
