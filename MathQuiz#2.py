#importing modules from tkinter
from tkinter import*
from tkinter import ttk

#Declaring parent class called MathsQuiz
class MathsQuiz:

    #Use __init__ method for all widgets
    def __init__(self,parent):

        #Widgets for welcome frame
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column =0)

        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                                bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                font = ("Time", 14, "bold italic"))
        self.TitleLabel.grid(columnspan = 2)

        self.NextButton = ttk.Button(self.Welcome, text = "Next")
        self.NextButton.grid(row = 8, column = 1)

        #Widgets for Questions frame
        self.Questions = Frame(parent)
        self.Questions.grid(row = 0, column = 1)

        #Label to show the question
        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                    bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                    font = ("Time", 14, "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)

        #Button for going to the next question
        self.HomeButton = ttk.Button(self.Questions, text = "Home")
        self.HomeButton.grid(row = 8, column = 1)

        

    #A function to remove the questions frame
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()

    def show_Questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()

        show_Welcome(self)

        
        
#Main routine
if __name__ == "__main__":
    root =Tk()
    frames = MathsQuiz(root)
    
    root.title("Quiz")
    root.mainloop()
    

        
        
