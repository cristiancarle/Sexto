from flask import Flask, request

app = Flask(__name__)

# Credenciales correctas
VALID_USERNAME = "admin"
VALID_PASSWORD = "secreto123"

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>
    </head>
    <body>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Usuario">
            <input type="password" name="password" placeholder="Contraseña">
            <input type="submit" value="Iniciar sesión">
        </form>
    </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return "Login exitoso!", 200
    return "Credenciales incorrectas", 401

if __name__ == '__main__':
    app.run(debug=True)