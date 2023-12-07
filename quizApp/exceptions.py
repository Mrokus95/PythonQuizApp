class NoQuestionsError(Exception):
    def __str__(self):
        return "No questions available for the quiz. Try again later."
