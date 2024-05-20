import tkinter as tk
from tkinter import messagebox
import random

class Player:
    def __init__(self, name, dob, student_id):
        self.name = name
        self.dob = dob
        self.student_id = student_id
        self.score = 0

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.configure(bg="#E6E6FA")  
        self.player = None

        self.player_name_label = tk.Label(self.root, text="Enter your name:", font=("Helvetica", 50), bg="#E6E6FA", fg="#4B0082")  
        self.player_name_label.pack(pady=20)
        
        self.player_name_entry = tk.Entry(self.root, font=("Helvetica", 50))
        self.player_name_entry.pack(pady=10)

        self.player_dob_label = tk.Label(self.root, text="Enter your date of birth (dd/mm/yyyy):", font=("Helvetica", 50), bg="#E6E6FA", fg="#4B0082")  
        self.player_dob_label.pack(pady=20)
        
        self.player_dob_entry = tk.Entry(self.root, font=("Helvetica", 50))
        self.player_dob_entry.pack(pady=10)

        self.player_id_label = tk.Label(self.root, text="Enter your student ID (numbers only):", font=("Helvetica", 50), bg="#E6E6FA", fg="#4B0082")  
        self.player_id_label.pack(pady=20)
        
        self.player_id_entry = tk.Entry(self.root, font=("Helvetica", 50))
        self.player_id_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Quiz", font=("Helvetica", 50), command=self.start_quiz, bg="#DDA0DD", fg="#4B0082")
        self.start_button.pack(pady=20)

    def start_quiz(self):
        player_name = self.player_name_entry.get().strip()
        player_dob = self.player_dob_entry.get().strip()
        player_id = self.player_id_entry.get().strip()
        if player_name and player_dob and player_id.isdigit():
            self.player = Player(player_name, player_dob, player_id)
            self.player_name_label.destroy()
            self.player_name_entry.destroy()
            self.player_dob_label.destroy()
            self.player_dob_entry.destroy()
            self.player_id_label.destroy()
            self.player_id_entry.destroy()
            self.start_button.destroy()
            self.initialize_quiz()
        else:
            messagebox.showerror("Error", "Please enter all the required information correctly.")

    def initialize_quiz(self):
        self.questions = [
            {"question": "What is the capital of France?", "answers": ["London", "Paris", "New York"], "correct": "Paris"},
            {"question": "What is 2 + 2?", "answers": ["3", "4", "5"], "correct": "4"},
            {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Jupiter", "Mars"], "correct": "Jupiter"},
            {"question": "Ngày quốc khánh Việt Nam là ngày nào?", "answers":["1/4","2/9","3/5", "2/9"], "correct":"2/9"},
        ]
        random.shuffle(self.questions) 
        self.score = 0
        self.current_question = 0
        self.time_left = 20
        self.timer_label = tk.Label(self.root, text="", font=("Helvetica", 50), bg="#E6E6FA", fg="#4B0082") 
        self.timer_label.pack(pady=10)
        self.create_widgets()
        self.display_question()
        self.start_timer()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 40), bg="#E6E6FA", fg="#4B0082")  
        self.question_label.pack(pady=30)
        
        self.answer_buttons = []
        for i in range(3):
            button = tk.Button(self.root, text="", font=("Helvetica", 40), width=30, command=lambda idx=i: self.check_answer(idx), bg="#DDA0DD", fg="#4B0082")  
            button.pack(pady=10)
            self.answer_buttons.append(button)
        
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 30), bg="#E6E6FA", fg="#4B0082")  
        self.score_label.pack(pady=10)
        
        self.next_button = tk.Button(self.root, text="Next", font=("Helvetica", 30), command=self.next_question, bg="#DDA0DD", fg="#4B0082")  
        self.next_button.pack(pady=5)

    def display_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])
        for i, answer in enumerate(question["answers"]):
            self.answer_buttons[i].config(text=answer)

    def check_answer(self, idx):
        selected_answer = self.questions[self.current_question]["answers"][idx]
        correct_answer = self.questions[self.current_question]["correct"]
        if selected_answer == correct_answer:
            self.player.score += 1
            self.score_label.config(text=f"Score: {self.player.score}")
        for button in self.answer_buttons:
            button.config(state=tk.DISABLED)

    def next_question(self):
        for button in self.answer_buttons:
            button.config(state=tk.NORMAL)
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.display_question()
            self.start_timer()
        else:
            result_message = f"{self.player.name}, your final score is {self.player.score}\n"
            result_message += f"Date of Birth: {self.player.dob}\n"
            result_message += f"Student ID: {self.player.student_id}"
            messagebox.showinfo("Quiz Completed", result_message)
            self.root.quit()

    def start_timer(self):
        self.time_left = 60
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
