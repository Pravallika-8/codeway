import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = {
            "high": [],
            "medium": [],
            "low": []
        }

        self.task_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Arial", 10, "bold"), bg="blue", fg="white")
        self.add_button.pack(pady=5)

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        self.high_priority_label = tk.Label(self.task_frame, text="High Priority", font=("Arial", 10, "bold"))
        self.high_priority_label.grid(row=0, column=0, padx=5, pady=5)

        self.med_priority_label = tk.Label(self.task_frame, text="Medium Priority", font=("Arial", 10, "bold"))
        self.med_priority_label.grid(row=0, column=1, padx=5, pady=5)

        self.low_priority_label = tk.Label(self.task_frame, text="Low Priority", font=("Arial", 10, "bold"))
        self.low_priority_label.grid(row=0, column=2, padx=5, pady=5)

        self.high_priority_listbox = tk.Listbox(self.task_frame, width=30, height=10, font=("Arial", 10))
        self.high_priority_listbox.grid(row=1, column=0, padx=5, pady=5)

        self.med_priority_listbox = tk.Listbox(self.task_frame, width=30, height=10, font=("Arial", 10))
        self.med_priority_listbox.grid(row=1, column=1, padx=5, pady=5)

        self.low_priority_listbox = tk.Listbox(self.task_frame, width=30, height=10, font=("Arial", 10))
        self.low_priority_listbox.grid(row=1, column=2, padx=5, pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Complete", command=self.mark_as_complete, font=("Arial", 10, "bold"), bg="green", fg="white")
        self.complete_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, font=("Arial", 10, "bold"), bg="red", fg="white")
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            priority = messagebox.askquestion("Priority", "Select task priority:", icon='info', type='yesnocancel')
            if priority == 'yes':
                self.tasks["high"].append((task, False))
                self.high_priority_listbox.insert(tk.END, task)
                self.high_priority_listbox.itemconfig(tk.END, {'bg': 'red'})
            elif priority == 'no':
                self.tasks["medium"].append((task, False))
                self.med_priority_listbox.insert(tk.END, task)
                self.med_priority_listbox.itemconfig(tk.END, {'bg': 'orange'})
            elif priority == 'cancel':
                self.tasks["low"].append((task, False))
                self.low_priority_listbox.insert(tk.END, task)
                self.low_priority_listbox.itemconfig(tk.END, {'bg': 'yellow'})
            self.task_entry.delete(0, tk.END)

    def mark_as_complete(self):
        selection_index = self.get_selected_task()
        if selection_index is not None:
            priority = self.get_task_priority(selection_index)
            if priority:
                if priority == "high":
                    self.high_priority_listbox.itemconfig(selection_index, {'bg': 'green'})
                    self.tasks["high"][selection_index] = (self.tasks["high"][selection_index][0], True)
                elif priority == "medium":
                    self.med_priority_listbox.itemconfig(selection_index, {'bg': 'green'})
                    self.tasks["medium"][selection_index] = (self.tasks["medium"][selection_index][0], True)
                elif priority == "low":
                    self.low_priority_listbox.itemconfig(selection_index, {'bg': 'green'})
                    self.tasks["low"][selection_index] = (self.tasks["low"][selection_index][0], True)

    def remove_task(self):
        selection_index = self.get_selected_task()
        if selection_index is not None:
            priority = self.get_task_priority(selection_index)
            if priority:
                if priority == "high":
                    del self.tasks["high"][selection_index]
                    self.high_priority_listbox.delete(selection_index)
                elif priority == "medium":
                    del self.tasks["medium"][selection_index]
                    self.med_priority_listbox.delete(selection_index)
                elif priority == "low":
                    del self.tasks["low"][selection_index]
                    self.low_priority_listbox.delete(selection_index)

    def get_selected_task(self):
        if self.high_priority_listbox.curselection():
            return self.high_priority_listbox.curselection()[0]
        elif self.med_priority_listbox.curselection():
            return self.med_priority_listbox.curselection()[0]
        elif self.low_priority_listbox.curselection():
            return self.low_priority_listbox.curselection()[0]
        return None

    def get_task_priority(self, index):
        if index is not None:
            if index < len(self.tasks["high"]):
                return "high"
            elif index < len(self.tasks["high"]) + len(self.tasks["medium"]):
                return "medium"
            elif index < len(self.tasks["high"]) + len(self.tasks["medium"]) + len(self.tasks["low"]):
                return "low"
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
