from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World TEAM ID: PNT2022TMID24878"

if __name__ == '__main__':
   app.run()