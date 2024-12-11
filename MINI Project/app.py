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

thank_you = [
    "Welcome, I will always assist you and Thank You"
]


hi = [
    "Hello, I am Health care chatBot,How can I assist you today?"

]



# Function to generate an appointment token
def generate_token():
    return f"APT-{random.randint(1, 999)}"

# Home route
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    doctor = request.form.get("doctor")
    date = request.form.get("date")
    time = request.form.get("time")

    # Save the data or process it
    return jsonify({"message": f"Appointment successfully booked with {doctor.capitalize()} on {date} at {time}."})








# Route for handling user queries
@app.route('/query', methods=['POST'])
def query():
    user_input = request.form.get("user_input", "").lower().strip()



    # Response logic

    if "appointment" in user_input:
        token = generate_token()
        response = f"Your appointment has been scheduled. Your token is {token}. Please mention it when you arrive."

    elif "doctor" in user_input or "specialty" in user_input:

        # Extract specialty from user input
        for specialty in doctors_info:
            if specialty in user_input:
                doctor = doctors_info[specialty]
                response = f"Our {specialty.capitalize()} specialist is {doctor['name']} with {doctor['experience']} experience. Available on {doctor['availability']}."
                break
        else:
            response = "We have specialists in doctor cardiology, doctor neurology, and doctor pediatrics. Please specify one of these."



    elif "health tip" in user_input:
        response = random.choice(health_tips)

    # elif "token" in user_input:
    #     response = random.choice(token)


    elif "hi" in user_input:
        response = random.choice(hi)
    
    elif "thank you" in user_input:
        response = random.choice(thank_you)
    else:
        response = "Welcome to Official Health Hospital! \t \"Ask about appointments, doctors, or health tips...\""

    return jsonify({"response": response})



if __name__ == '__main__':
    app.run(debug=True)








