from flask import Flask
from config import env
from find_card.route import card

# Get env
new_env = env.Env().__dict__
port = new_env.get("port")
debug = new_env.get("debug")

app = Flask(__name__)

app.register_blueprint(card)

if __name__=='__main__':
    app.run(debug=debug, port=port)