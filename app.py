import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message'].lower()  

    
    if user_message in ["hi", "hello", "hey", "howdy"]:
        bot_response = "hello! how can I assist you today?"
    elif "how are you" in user_message:
        bot_response = "I'm just a chatbot, but I'm doing great! How can I help you?"
    elif "help" in user_message:
        bot_response = (
            "Sure! I can help you with the following:\n"
            "1. Schedule an appointment\n"
            "2. Find a doctor\n"
            "3. Get information on hospital services\n"
            "4. Understand health insurance options\n"
            "Please let me know what you need assistance with!"
        )
    elif "appointment" in user_message:
        bot_response = "To schedule an appointment, please provide your name, the doctor you want to see, and your preferred date and time."
    elif "doctor" in user_message:
        bot_response = "You can find a doctor by specialty. Please tell me which specialty you are looking for."
    elif "dentist" in user_message:
        bot_response = "Great choice! We have several dentists available. Please provide your preferred date and time."

    
    elif re.search(r'\b(\d{1,2}/\d{1,2}/\d{4})\b', user_message) or re.search(r'\b(\d{1,2}:\d{2})\b', user_message):
        date_match = re.search(r'\b(\d{1,2}/\d{1,2}/\d{4})\b', user_message)
        time_match = re.search(r'\b(\d{1,2}:\d{2})\b', user_message)
        date_str = date_match.group(0) if date_match else "a specified date"
        time_str = time_match.group(0) if time_match else "a specified time"
        bot_response = f"Your appointment has been scheduled for {date_str} at {time_str}. Please arrive at least 15 minutes early."

    elif "emergency care" in user_message:
        bot_response = "For emergency care, please go to our emergency department. If you need immediate assistance, call 911 or our emergency hotline."

    elif "insurance" in user_message:
        bot_response = "Yes, we accept various health insurance plans. Please check with our insurance office for specific details."
    
    elif any(word in user_message for word in ["okay", "thanks", "thank you", "alright", "got it", "appreciate it"]):
        bot_response = "You're welcome! If you have any more questions or need assistance, feel free to ask."

    else:
        bot_response = "Sorry, I didn't understand that. Can you please rephrase?"

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)

