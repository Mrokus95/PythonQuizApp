from datetime import datetime, timedelta

class QuizLogic:
    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.fastest_answer_time = None
        self.slowest_answer_time = None
        self.quiz_start_time = datetime.now()
        self.quiz_end_time = None
        self.question_start_time = None
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        """To check if the quiz has more questions"""

        return self.question_no < len(self.questions)

    def next_question(self):
        """Get the next question by incrementing the question number"""

        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        self.question_start_time = datetime.now()
        q_text = self.current_question.question_text
        return f"Question {self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Check the user's answer against the correct answer and maintain the score"""

        question_end_time = (
            datetime.now()
        )

        if (
            self.fastest_answer_time is None
            or (question_end_time - self.question_start_time) < self.fastest_answer_time
        ):
            self.fastest_answer_time = question_end_time - self.question_start_time

        if (
            self.slowest_answer_time is None
            or (question_end_time - self.question_start_time) > self.slowest_answer_time
        ):
            self.slowest_answer_time = question_end_time - self.question_start_time

        if user_answer.lower() == self.current_question.correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def format_time(self, timedelta):
        """Formatuje czas w mikrosekundach do postaci sekundy.milisekundy"""
        seconds = timedelta.total_seconds()
        formatted_time = f"{seconds:.2f}"
        return formatted_time

    def get_score(self):
        """Get the number of correct answers, wrong answers, and score percentage."""

        quiz_end_time = datetime.now()
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        fastest_answer_time = self.format_time(self.fastest_answer_time)
        slowest_answer_time = self.format_time(self.slowest_answer_time)

        avg_answer_time = (quiz_end_time - self.quiz_start_time) / self.question_no
        avg_answer_time = self.format_time(avg_answer_time)

        return (
            self.score,
            wrong,
            score_percent,
            fastest_answer_time,
            slowest_answer_time,
            avg_answer_time,
        )

if __name__ == "__main__":
    pass