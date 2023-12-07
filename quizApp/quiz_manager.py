from tkinter import Tk, Button, Toplevel, Label, messagebox
from .quiz_logic import QuizLogic
from .quiz_ui import QuizInterface
from .quiz_questions import QuestionManager
from random import shuffle
from .exceptions import NoQuestionsError

class QuizManager:
    def __init__(self):
        self.question_manager = QuestionManager()
        self.quiz = None
        self.quiz_ui = None

    def start_quiz(self):
        try:
            if self.quiz_ui is not None:
                self.quiz_ui.window.destroy()

            question_bank = self.question_manager.get_question_bank()

            if not question_bank:
                raise NoQuestionsError

            self.quiz = QuizLogic(question_bank)
            self.quiz_ui = QuizInterface(self.quiz, self)

        except NoQuestionsError as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", str(e))
            exit()
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", "An unexpected error occurred. Try again later.")
            exit()
