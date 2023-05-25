from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='',
            fill=THEME_COLOR,
            width=200,
            font=("Arial", 15))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text='Score:0', fg="white", bg=THEME_COLOR)  # use fg for label color
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)

        self.true.grid(row=2, column=0)
        self.false.grid(row=2, column=1)

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
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
