from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample data for doctors and health tips
doctors_info = {
    "cardiology": {"name": "Dr. Smith", "experience": "10 years", "availability": "Mon, Wed, Fri"},
    "neurology": {"name": "Dr. Doe", "experience": "8 years", "availability": "Tue, Thu"},
    "pediatrics": {"name": "Dr. Clark", "experience": "5 years", "availability": "Mon-Fri"},
}

health_tips = [
    "Drink plenty of water to stay hydrated.",
    "Exercise regularly for at least 30 minutes a day.",
    "Get regular check-ups with your healthcare provider.",
]

# Function to generate an appointment token
def generate_token():
    return f"APT-{random.randint(1000, 9999)}"

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling user queries
@app.route('/query', methods=['POST'])
def query():
    user_input = request.form.get("user_input").lower()

    # Response logic
    if "appointment" in user_input:
        token = generate_token()
        response = f"Your appointment has been scheduled. Your token is {token}. Please mention it when you arrive."
    elif "doctor" in user_input or "specialty" in user_input:
        specialty = user_input.split()[-1]
        doctor = doctors_info.get(specialty)
        if doctor:
            response = f"Our {specialty.capitalize()} specialist is {doctor['name']} with {doctor['experience']} experience. Available on {doctor['availability']}."
        else:
            response = "We have specialists in cardiology, neurology, and pediatrics. Please specify one of these."
    elif "health tip" in user_input:
        response = health_tips[random.randint(0, len(health_tips) - 1)]
    else:
        response = "Welcome to Official Health Hospital! How can I assist you today?"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
