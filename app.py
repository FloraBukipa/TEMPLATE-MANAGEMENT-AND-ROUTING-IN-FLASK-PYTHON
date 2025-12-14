from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', title='Home', message="Hello from Flask!",user={
        'NAME:':'AKINTAN ROBERT',
        'PROGRAMMING LANGUAGE:':'PYTHON',
        'FRAMEWORK:':'FLASK',
        'HOBBIES:':'TRAVELLING, CODING, READING'
    }
                           )

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/services')
def services():
    return render_template('services.html', title='Our Services Us')



if __name__ == '__main__':
    app.run(debug=True)
