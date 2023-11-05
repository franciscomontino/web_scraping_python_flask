# MTG cheapest price finder

This is a service built with Python, Flask and Selenium dedicated to finding the best MTG cards prices on some websites

### Installation
First, create new virtual enviroment and activate it
```
python -m venv venv
. .venv/bin/activate
```

Install needed dependences
```
pip install Flask
pip install python-dotenv
```

### Run project
```
python3 main.py
```

### Enviroment variables
```
SCG_URL=https://starcitygames.com/
CK_URL=https://www.cardkingdom.com/
DEBUG=True
PORT=3000
```

### Endpoit

Post endpoint
```
http://127.0.0.1:{port}/card/get_card
```

Body request
```
{
    "card_name": "card name"
}
```