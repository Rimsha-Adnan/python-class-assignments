# General Knowledge Quiz using OOP in Python

# Define a Question class to encapsulate each quiz question
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text  # String: The quiz question
        self.options = options              # List: Multiple choice options
        self.correct_answer = correct_answer  # String: Correct answer (e.g., 'A', 'B', etc.)

    def is_correct(self, user_answer):
        # Check if the user's answer matches the correct answer
        return user_answer.strip().upper() == self.correct_answer.strip().upper()


# Define a Quiz class to handle quiz logic
class Quiz:
    def __init__(self):
        self.questions = []  # List of Question objects
        self.score = 0       # User's score

    def add_question(self, question):
        # Add a new question to the quiz
        self.questions.append(question)

    def start(self):
        print("🧠 Welcome to the General Knowledge Quiz!")
        print("----------------------------------------")
        for idx, question in enumerate(self.questions, 1):
            print(f"\nQuestion {idx}: {question.question_text}")
            for option in question.options:
                print(option)
            user_answer = input("Your answer (A/B/C/D): ")
            if question.is_correct(user_answer):
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer was {question.correct_answer}")

        print("\n🎉 Quiz Over!")
        print(f"Your final score: {self.score}/{len(self.questions)}")
        self.evaluate_performance()

    def evaluate_performance(self):
        # Evaluate and display performance message based on score
        if self.score == len(self.questions):
            print("🌟 Amazing! You got all answers correct!")
        elif self.score >= len(self.questions) // 2:
            print("👍 Good job! You know quite a bit!")
        else:
            print("📘 Keep learning! You'll do better next time.")


# Main function to run the quiz
def main():
    # Instantiate the Quiz object
    quiz = Quiz()

    # Add quiz questions (can be expanded)
    quiz.add_question(Question(
        "What is the capital of France?",
        ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "C"
    ))

    quiz.add_question(Question(
        "Who wrote 'Hamlet'?",
        ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "B"
    ))

    quiz.add_question(Question(
        "What planet is known as the Red Planet?",
        ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "C"
    ))

    quiz.add_question(Question(
        "What is the chemical symbol for gold?",
        ["A. Au", "B. Ag", "C. Gd", "D. Go"],
        "A"
    ))

    quiz.add_question(Question(
        "In which year did World War II end?",
        ["A. 1939", "B. 1945", "C. 1918", "D. 1950"],
        "B"
    ))

    quiz.add_question(Question(
        "Which is the largest ocean on Earth?",
        ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "D"
    ))

    quiz.add_question(Question(
        "What is the square root of 64?",
        ["A. 6", "B. 8", "C. 10", "D. 12"],
        "B"
    ))

    quiz.add_question(Question(
        "Which continent is the Sahara Desert located in?",
        ["A. South America", "B. Asia", "C. Africa", "D. Australia"],
        "C"
    ))

    quiz.add_question(Question(
        "What is the boiling point of water at sea level (in Celsius)?",
        ["A. 90", "B. 95", "C. 100", "D. 105"],
        "C"
    ))

    quiz.add_question(Question(
        "Which language is the most spoken in the world?",
        ["A. English", "B. Mandarin Chinese", "C. Hindi", "D. Spanish"],
        "B"
    ))

    # Start the quiz
    quiz.start()


# Run the application
if __name__ == "__main__":
    main()
