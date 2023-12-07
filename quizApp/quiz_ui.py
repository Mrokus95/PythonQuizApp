from tkinter import (
    Tk,
    Canvas,
    StringVar,
    Label,
    Radiobutton,
    Button,
    messagebox,
    Frame,
    Toplevel,
)
from .quiz_logic import QuizLogic
from .settings import theme_color, font


class QuizInterface:
    def __init__(self, quiz_logic: QuizLogic, quiz_manager) -> None:
        self.quiz = quiz_logic
        self.quiz_manager = quiz_manager
        self.window = Tk()
        self.window.title("Quiz application")
        self.window.geometry("800x800")
        self.create_widgets()

    def create_widgets(self):

        self.display_title()

        self.category_label = Label(
            self.window, text="Category:", font=(font, 15, "italic")
        )
        self.category_label.pack()

        self.tags_label = Label(self.window, text="Tags:",
        font=(font, 15, "italic"))
        self.tags_label.pack()

        question_frame = Frame(self.window)
        question_frame.pack(pady=20)

        self.canvas = Canvas(question_frame, width=800, height=350)
        self.canvas.grid(row=0, column=0, pady=10)
        self.question_text = self.canvas.create_text(
            400,
            80,
            text="Question here",
            width=680,
            fill=theme_color,
            font=(font, 15, "italic"),
        )
        self.display_question()

        self.user_answer = StringVar()

        self.opts = self.radio_buttons()
        self.display_options()

        self.feedback = Label(self.window, pady=40, font=(font, 15, "bold"))
        self.feedback.pack()

        self.buttons()

        self.window.resizable(False, False)

        self.window.mainloop()

    def display_title(self):
        """To display title"""

        title = Label(
            self.window,
            text="Quiz Application",
            width=50,
            bg="green",
            fg="white",
            font=(font, 20, "bold"),
        )
        title.pack(pady=5)

    def display_question(self):
        """To display the question"""
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

        category_text = f"Category: {self.quiz.current_question.question_category}"
        tags_text = f"Tags: {', '.join(self.quiz.current_question.question_tags)}"

        self.category_label.config(text=category_text)
        self.tags_label.config(text=tags_text)

    def radio_buttons(self):
        """To create four options (radio buttons)"""

        choice_list = []

        y_pos = 250

        while len(choice_list) < 4:
            radio_btn = Radiobutton(
                self.window,
                text="",
                variable=self.user_answer,
                value="",
                font=(font, 14),
            )

            choice_list.append(radio_btn)

            radio_btn.place(x=150, y=y_pos)

            y_pos += 40

        return choice_list

    def display_options(self):
        """To display four options"""

        val = 0
        self.user_answer.set(None)

        for option in self.quiz.current_question.choices:
            self.opts[val]["text"] = option
            self.opts[val]["value"] = option
            val += 1

    def new_game(self):
        user_response = messagebox.askyesno(
            "New Game", "Are you sure you want to start a new game?"
        )
        if user_response:
            self.window.destroy()
            self.quiz_manager.start_quiz()

    def buttons(self):
        """To show next button and quit button"""

        self.next_button = Button(
            self.window,
            text="Next",
            command=self.next_btn,
            width=10,
            bg="green",
            fg="white",
            font=(font, 16, "bold"),
        )

        self.next_button.place(x=325, y=430)

        quit_button = Button(
            self.window,
            text="Quit",
            command=self.window.destroy,
            width=5,
            bg="red",
            fg="white",
            font=(font, 16, " bold"),
        )

        quit_button.place(x=700, y=50)

        self.new_game_button = Button(
            self.window,
            text="New Game",
            command=self.new_game,
            width=10,
            bg="blue",
            fg="white",
            font=(font, 16, "bold"),
        )

    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = "Correct answer! \U0001F44D"
        else:
            self.feedback["fg"] = "red"
            self.feedback["text"] = (
                "\u274E Oops! \n"
                f"The right answer is: {self.quiz.current_question.correct_answer}"
            )

        if self.quiz.has_more_questions():
            self.display_question()
            self.display_options()
        else:
            self.display_result()
            self.next_button.pack_forget()
            self.new_game_button.place(x=325, y=430)

    def display_result(self):
        """To display the result using a new window"""

        (
            correct,
            wrong,
            score_percent,
            fastest,
            slowest,
            avg_answer_time,
        ) = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"
        fastest = f"Fastest answer: {fastest}"
        slowest = f"Slowest answer: {slowest}"
        avg_answer_time = f"Avg answer time: {avg_answer_time}"
        result = f"Score: {score_percent}%"

        result = (
            f"{result}\n{correct}\n{wrong}\n{fastest}\n{slowest}\n{avg_answer_time}"
        )

        result_window = Toplevel(self.window)
        result_window.title("Result")

        if score_percent <= 50:
            color = "red"
        elif score_percent <= 75:
            color = "orange"
        elif score_percent <= 90:
            color = "green"
        else:
            color = "blue"

        result_label = Label(
            result_window, text=result, font=(font, 14), bg=color, padx=20, pady=20
        )
        result_label.pack()

        close_button = Button(
            result_window,
            text="Close",
            command=result_window.destroy,
            font=(font, 12),
        )
        close_button.pack(pady=10)

if __name__ == "__main__":
    pass