import tkinter as tk
import random


def space():
    canvas = tk.Canvas(root, height=30)
    canvas.pack()

class Quiz(tk.Frame):
    def __init__(self, parent, questions):
        tk.Frame.__init__(self, parent)
        
        self.questions = questions
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(self, text=self.questions[self.current_question]['question'], font=('Helvetica', 14))
        self.question_label.pack(pady=20)
        
        self.answer_buttons = []
        for answer in self.questions[self.current_question]['answers']:
            answer_button = tk.Button(self, text=answer, command=lambda answer=answer: self.check_answer(answer))
            answer_button.pack(pady=5)
            self.answer_buttons.append(answer_button)
        
        self.score_label = tk.Label(self, text="Score: {}".format(self.score))
        self.score_label.pack(pady=20)
        
        self.next_question_button = tk.Button(self, text="Next question", state=tk.DISABLED, command=self.next_question)
        self.next_question_button.pack(pady=10)
        
    def check_answer(self, answer):
        if answer == self.questions[self.current_question]['correct_answer']:
            self.score += 1
            self.score_label.config(text="Score: {}".format(self.score))
        
        for button in self.answer_buttons:
            button.config(state=tk.DISABLED)
        
        self.next_question_button.config(state=tk.NORMAL)
    
    def next_question(self):
        self.current_question += 1
        
        if self.current_question >= len(self.questions):
            self.question_label.config(text="Quiz complete!")
            for button in self.answer_buttons:
                button.destroy()
            self.next_question_button.destroy()
        else:
            self.question_label.config(text=self.questions[self.current_question]['question'])
            for i, answer in enumerate(self.questions[self.current_question]['answers']):
                self.answer_buttons[i].config(text=answer, state=tk.NORMAL)
            self.next_question_button.config(state=tk.DISABLED)

# Open the text file containing the questions and answers
with open('questions.txt', 'r') as file:
    lines = file.readlines()

# Create the list of questions as a list of dictionaries
questions = []
questions = [
    {
        'question': 'Co to jest przypadek testowy?',
        'answers': ['Zbiór danych wejściowych, wstępnych warunków wykonania, oczekiwanych rezultatów i końcowych warunków', 
                    'Test2', 'Test3', 'Test4'],
        'correct_answer': 'Warszawa'
    },
    {
        'question': 'Ile to 1 + 1',
        'answers': ['2', '3', '4', '5'],
        'correct_answer': '2'
    },
    {
        'question': 'Co to jest ISTQB',
        'answers': ['Test1', 'Test2', 'Test3', 'Test4'],
        'correct_answer': 'Test3'
    }
]


root = tk.Tk()
root.geometry("400x400")
quiz = Quiz(root, questions)
quiz.pack(fill=tk.BOTH, expand=True)
root.mainloop()


