from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """show homepage"""

    return """
        <html>
            <body>
                <h1>I am the home page</h1>
            </body>
        </html>
        """

@app.route('/welcome')
def welcome():
    """show welcome text page"""

    return """
         <html>
            <body>
                <h1>Welcome!</h1>
            </body>
        </html>
        """

@app.route('/welcome/home')
def welcome_home():
    """show welcome text page"""

    return """
         <html>
            <body>
                <h1>Welcome home!</h1>
            </body>
        </html>
        """

@app.route('/welcome/back')
def welcome_back():
    """show welcome text page"""

    return """
         <html>
            <body>
                <h1>Welcome back!</h1>
            </body>
        </html>
        """