from question_model import Question
from data import question_data
question_bank=[]
from quiz_brain import QuizBrain
for q_data in question_data:
    question_bank.append(Question(q_data["question"],q_data["correct_answer"]))
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You ve completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")