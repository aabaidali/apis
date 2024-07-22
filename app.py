from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    quiz = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correctAnswer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "correctAnswer": "Mars"},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "correctAnswer": "Pacific"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"], "correctAnswer": "Harper Lee"},
        {"question": "What is the smallest country in the world?", "options": ["Vatican City", "Monaco", "Nauru", "San Marino"], "correctAnswer": "Vatican City"}
    ]
    return jsonify(quiz)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
