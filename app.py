"""
This code creates a Flask app (web application) using the 'flask' library that allows conversion of temperatures between different measurement scales. The application imports the necessary libraries including the temperature conversion functions, creates an app instance and defines the route /convert and endpoint to the app. This route takes the temperature and conversion type from the request body and uses an if-else statement to convert the temperature accordingly and return the result as a JSON object. Finally, the app provides a route for a homepage and runs the app.
"""
# Import the necessary libraries
from flask import Flask, request, jsonify, render_template

# Import the temperature conversion functions from the conversions module
from conversions import fahr2cel, cel2fahr, fahr2kel, kel2fahr, cel2kel, kel2cel


# Create a Flask app
app = Flask(__name__)

# Define the route for the /convert endpoint


@app.route('/convert', methods=['POST'])
def convert():
    # Get the temperature and conversion type from the request body
    data = request.get_json()
    temp = float(data['temp'])
    conversion = data['conversion']

    print(f"temp: {temp}, conversion: {conversion}")

    # Convert the temperature using appropriate function
    if conversion == "fahr2cel":
        result = fahr2cel(temp)
    elif conversion == "cel2fahr":
        result = cel2fahr(temp)
    elif conversion == "fahr2kel":
        result = fahr2kel(temp)
    elif conversion == "kel2fahr":
        result = kel2fahr(temp)
    elif conversion == "cel2kel":
        result = cel2kel(temp)
    elif conversion == "kel2cel":
        result = kel2cel(temp)
    else:
        result = None

    print(f"Your Result: {result}")

    # Return the result as a JSON object
    return jsonify({'result': result})


# Define a route for the homepage


@app.route('/')
def index():
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run()
