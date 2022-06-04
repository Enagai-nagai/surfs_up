from flask import Flask
app = Flack(__name__)

@app.route('/')
def home():
    print("Server received request for 'Home' page...")
    return "<h1>Welcome to my 'Home' Page"

if__name__ == "__main__":
    app return home()