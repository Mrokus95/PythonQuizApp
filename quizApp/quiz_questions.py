import requests
from random import shuffle
import html
from tkinter import Tk, Label, Entry, Listbox, Button, StringVar, messagebox
from tkinter.ttk import Combobox
from pathlib import Path
from .question_model import Question
import json
from .exceptions import NoQuestionsError
from .settings import limit_api_questions, api_url, questions_quantity_in_quiz


class QuestionManager:
    def __init__(self):
        self.question_bank = []

    def get_questions_from_api(self, limit=limit_api_questions):
        parameters = {
            "limit": limit,
        }

        try:
            response = requests.get(
                url=api_url, params=parameters
            )
            response.raise_for_status()
            question_data = response.json()

            question_bank = []

            for question_info in question_data:
                question = question_info["question"]
                question_text = html.unescape(question["text"])
                question_tags = html.unescape(question_info["tags"])
                question_difficulty = html.unescape(question_info["difficulty"])
                question_category = html.unescape(question_info["category"])
                correct_answer = html.unescape(question_info["correctAnswer"])
                incorrect_answers = question_info["incorrectAnswers"]

                choices = []
                for ans in incorrect_answers:
                    choices.append(html.unescape(ans))
                choices.append(correct_answer)
                shuffle(choices)

                new_question = Question(
                    question_text,
                    correct_answer,
                    choices,
                    question_tags,
                    question_difficulty,
                    question_category,
                )
                self.question_bank.append(new_question)
            return new_question
        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")


    def load_questions(self):
        self.question_bank = []
        api_questions = self.get_questions_from_api()

        if api_questions is None:
            user_response = messagebox.askyesno(
                "Question Manager",
                "We have a problem with the API. Do you want to continue with your own questions?"
            )
            if not user_response:
                raise Exception("Failed to load questions from API")
            else:
                user_questions = self.add_user_questions()
                self.question_bank.extend(user_questions)

        user_response = messagebox.askyesno(
            "Question Manager", 
            "Do you want to add your own questions additionally to the question base?"
        )

        if user_response:
            user_questions = self.add_user_questions()
            self.question_bank.extend(user_questions)
        return True

    def add_user_questions(self):
        root = Tk()
        editor = QuestionEditor(root)
        root.mainloop()
        return editor.get_user_questions()

    def get_question_bank(self, limit=questions_quantity_in_quiz):
        try:
            self.load_questions()
        except:
            raise NoQuestionsError
        shuffle(self.question_bank)
        return self.question_bank[:limit]


class QuestionEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Question Editor")
        self.user_questions = []

        self.labels = [
            "Question",
            "Correct Answer",
            "Choices (comma-separated)",
            "Tags (comma-separated)",
            "Difficulty",
            "Category",
        ]
        self.entries = {label: Entry(root, width=40) for label in self.labels}

        self.difficulty_options = ["Easy", "Medium", "Hard"]
        self.difficulty_var = StringVar()
        self.difficulty_combobox = Combobox(
            root,
            textvariable=self.difficulty_var,
            values=self.difficulty_options,
            state="readonly",
            width=37,
        )
        self.difficulty_combobox.set(self.difficulty_options[0])

        self.add_button = Button(root, text="Add Question", 
        command=self.add_question)
        self.finish_button = Button(root, text="Finish Editing", 
        command=self.finish_editing)

        self.arrange_widgets()

    def arrange_widgets(self):
        for i, label in enumerate(self.labels):
            Label(self.root, text=label).grid(row=i, column=0, sticky="e")
            if label == "Difficulty":
                self.difficulty_combobox.grid(
                    row=i, column=1, pady=5, padx=5, columnspan=2
                )
            else:
                self.entries[label].grid(row=i, column=1, pady=5, 
                padx=5, columnspan=2)

        self.add_button.grid(row=len(self.labels) + 1, column=0, columnspan=2, 
        pady=10, padx=5)
        self.finish_button.grid(row=len(self.labels) + 1, column=2, pady=10, 
        padx=5)

    def add_question(self):
        question_text = self.entries["Question"].get()
        correct_answer = self.entries["Correct Answer"].get()
        choices_str = self.entries["Choices (comma-separated)"].get()
        tags = self.entries["Tags (comma-separated)"].get()
        difficulty = self.difficulty_var.get()
        category = self.entries["Category"].get()

        choices = [choice.strip() for choice in choices_str.split(",")]

        try:
            new_question = Question(
                question_text,
                correct_answer,
                choices,
                tags,
                difficulty,
                category,
            )
            self.user_questions.append(new_question)
            for entry in self.entries.values():
                entry.delete(0, 'end')
            self.difficulty_combobox.set(self.difficulty_options[0])
            messagebox.showinfo("Success", "Question added successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def finish_editing(self):
        self.root.destroy()

    def get_user_questions(self):
        return self.user_questions

if __name__ == "__main__":
    pass