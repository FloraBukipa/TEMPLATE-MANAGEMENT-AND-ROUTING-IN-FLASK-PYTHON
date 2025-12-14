# TEMPLATE-MANAGEMENT-AND-ROUTING-IN-FLASK-PYTHON
In Flask, routing maps URLs to specific Python functions using the @app.route() decorator, while template management uses the Jinja2 engine and the render_template() function to generate dynamic HTML content. 
#Routing in Flask
Routing is the mechanism that determines which function in your Python application should handle a specific URL request. 
PYTHON FILE (app.py)
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

@app.route() Decorator: This is the primary way to define a route. The decorator binds the function below it to the specified URL path.
#Template Management in Flask
Flask uses the Jinja2 templating engine to manage and render dynamic HTML pages. Templates allow you to separate presentation logic from application logic. 
templates folder: Flask automatically looks for template files in a directory named templates located in your application's root directory.
render_template() function: Instead of returning raw HTML strings from your view functions, you use this function to render a template file and pass data to it.
#Project Structure:
Flask applications, by default, expect templates and static files to be located in specific folders within the application's root directory :

 
app.py: This is the main application file (or a package, in larger projects) where your Flask app instance and primary routes are defined.
/templates: Flask automatically looks for HTML template files in this specific directory. You can use subdirectories (e.g., /templates) to further organize related templates. You keep html files here.
/static: This folder is where you place static assets like CSS files, JavaScript files, and images. 
#Template Inheritance
A key feature is template inheritance, which allows you to define a base layout (base.html) and have other templates inherit and override specific blocks of content.
#templates/base.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Flask App - {{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">

</head>
<body>

    {% include 'includes/navbar.html' %}
    <div class="wrapper">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
#templates/home.html (child template):
{% extends 'base.html' %}
{% block content %}
    <h1>Welcome to the Home Page!</h1>
    <p>This is the main content.</p>

      <h1>{{ message }}</h1>
    <table border="1">
        <thead>
            <tr>
                <th>USER DETAILS</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            {% for key, value in user.items() %}
            <tr>
                <td>{{ key }}</td>
                <td>{{ value }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
#Navigation File 
It is a common and recommended practice in Flask development to place partial templates like a navigation bar file (e.g., _nav.html or nav.html) in a subfolder within the main templates directory e.g. template/include/navbar.html. This aids in project organization, though Flask does not strictly enforce it.
template/include/navbar.html.
<div id='menuHolder'>
   <div class="menu active"><a href="{{ url_for('index') }}">Home</a></div> 

   <div class="menu"> <a href="{{ url_for('about') }}">About</a></div>

<div class="menu"> <a href="{{ url_for('services') }}">Services</a></div>
</div>
#static/main.css:
It is standard Flask convention to have a static folder in your project's root directory (alongside app.py and the templates folder) to hold CSS, JavaScript, images, etc., which Flask automatically serves from the /static URL path. You then link these files in your HTML templates using url_for('static', filename='path/to/your/file.css'), allowing for organized assets and easy updates.
*{
  box-sizing: border-box;
  margin:0;
  padding: 0;
}
.wrapper{
  width: 900px;
  min-height: 600px;
  margin: 0 auto;
  border:1px dotted #ccc;
  padding: 20px;
}

#menuHolder{
  width:100%;
  height: 50px;
  display: flex;
  background-color: blueviolet;
  align-items: center;
  justify-items: center;
  justify-content: center;
  align-content: center;
}
.menu a{
  color:white;
  text-decoration: none;
}
.menu{
  width: 100px;
  height: 100%;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;

}
#menuHolder .icon{
  width: 80px;
  color:white;
}
#menuHolder .icon:hover{
color:gold;
cursor: pointer;
}
#menuHolder .active{
  background-color: gold;
  color: red;
}
#menuHolder .active:hover{
  background-color: black;
  color: gold;
}
.menu:hover{
  background-color: black;
  color: gold;
}
#logoHolder{
  width: 100px;
  height: 50px;
  margin-right: 100px;
  display: flex;
  align-items: center;
  justify-items: center;
  padding: 5px;
}
#menuHolder img{
  width: 100%;
  height:100%;
}

#cardHolder{
  display: flex;
justify-content: center;
flex-wrap: wrap;
}
.ProductCard{
  width: 200px;
  height: 250px;
  border:1px solid red;
  margin: 10px;
}

.ProductCard{
  display: flex;
  flex-direction: column;
  text-align: center;
}

.ProductCard .ProductTitle{
  font-weight: bold;
}

.ProductCard .ProductImage{
  width:100%;
  height: 120px;
  background-color: aqua;
}

.ProductCard .ProductImage img{
  width:100%;
  height: 100%;

}

