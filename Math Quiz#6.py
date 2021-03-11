from tkinter import *
from tkinter import ttk
from random import *


class MathQuiz:
    def __init__(self, parent):
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.TitleLabel = Label(self.Welcome, text="Welcome to Maths Quiz",
                                bg="black", fg="white", width=20, padx=30, pady=10,
                                font=("Time", '14', "bold italic"))
        self.TitleLabel.grid(columnspan=2)

        self.NextButton = ttk.Button(self.Welcome, text="Next", command=self.show_questions)
        self.NextButton.grid(row=10, column=0, columnspan=2, pady=10)

        """Widgets for Questions Frame"""
        self.Questions = Frame(parent)
        self.Questions.grid(row=0, column=1)

        self.QuestionsLabel = Label(self.Questions, text="Quiz Questions", bg="black", fg="white",
                                    width=30, padx=30, pady=10, font=("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan=2)

        self.Problems = Label(self.Questions, text="")
        self.Problems.grid(row=1, column=0)

        self.AnswerEntry = ttk.Entry(self.Questions, width=20)
        self.AnswerEntry.grid(row=1, column=1)

        self.feedback = Label(self.Questions, text="")
        self.feedback.grid(row=2, column=0)

        self.next_button = ttk.Button(self.Questions, text="Next Question", width=20, command=self.next_question)
        self.next_button.grid(row=8, column=1)

        self.check_button = ttk.Button(self.Questions, text="Check answer", command=self.check_answer)  # HEREEEEEEEEEE
        self.check_button.grid(row=8, column=0)

        """Widgets for the Welcome Frame"""
        self.NameLabel = Label(self.Welcome, text="Name", anchor=W, fg="black", width=17, pady=10,
                               font=("Time", "12", "bold italic"))
        self.NameLabel.grid(row=1, column=1, columnspan=5)

        self.NameEntry = ttk.Entry(self.Welcome, width=20)
        self.NameEntry.grid(row=2, column=0, columnspan=2)

        self.AgeLabel = Label(self.Welcome, text="Age", anchor=W, width=16, fg="black", pady=10,
                              font=("Time", "12", "bold italic"))
        self.AgeLabel.grid(row=3, column=1, columnspan=2)

        self.AgeEntry = ttk.Entry(self.Welcome, width=20)
        self.AgeEntry.grid(row=4, column=0, columnspan=2)

        self.WarningLabel = Label(self.Welcome, text="", anchor=W, fg="red", width=20, padx=30, pady=10)
        self.WarningLabel.grid(row=5, columnspan=2)

        self.DifficultyLabel = Label(self.Welcome, text="Choose Difficulty level", anchor=W,
                                     fg="black", width=20, pady=10, font=("Time", '12', 'bold italic'))
        self.DifficultyLabel.grid(row=6, column=0, columnspan=2)

        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            self.rb = Radiobutton(self.Welcome, variable=self.diff_lvl, value=i, text=self.difficulty[i],
                                  anchor=W, padx=50, width="5", height="1")
            self.diff_btns.append(self.rb)
            self.rb.grid(row=i + 7, column=0, columnspan=2)

        self.Questions.grid_remove()

    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text="Correct")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()
            else:
                self.feedback.configure(text="Incorrect")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()
        except ValueError:
            self.feedback.configure(text="Enter a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()

    def show_welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()

    def show_questions(self):
        try:
            if self.NameEntry.get() == "":
                self.WarningLabel.configure(text="Please Enter Name")
                self.NameEntry.focus()

            elif self.NameEntry.get().isalpha() == False:
                self.WarningLabel.configure(text="PLease enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()
            elif self.AgeEntry.get() == "":
                self.WarningLabel.configure(text="PLease Enter age")
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) > 12:
                self.WarningLabel.configure(text="You are too old!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) < 0:
                self.WarningLabel.configure(text="You are too old!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) < 7:
                self.WarningLabel.configure(text="You are too young")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            else:
                self.Welcome.grid_remove()
                self.Questions.grid()
                self.next_question()

        except ValueError:
            self.WarningLabel.configure(text="Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

    def next_question(self):
        """Creates questions and stores answer"""
        x = randrange(10)
        y = randrange(10)
        self.answer = x + y

        question_text = str(x) + " + " + str(y) + " = "
        self.Problems.configure(text=question_text)

    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text="Correct")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()

            else:
                self.feedback.configure(text="Incorrect")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()

        except ValueError:
            self.feedback.configure(text="Enter a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()


# Main routine
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
