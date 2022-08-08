from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial", 10, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.true_image = PhotoImage(file="images//true.png")
        self.false_image = PhotoImage(file="images//false.png")

        self.true_button = Button(image=self.true_image, width=100, height=97,
                                  highlightthickness=0, bg=THEME_COLOR, command=self.true_ans)
        self.false_button = Button(image=self.false_image, width=100, height=97,
                                   highlightthickness=0, bg=THEME_COLOR, command=self.false_ans)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_ans(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_ans(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
