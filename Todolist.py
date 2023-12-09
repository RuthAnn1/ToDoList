import heapq
import tkinter as tk
from tkinter import simpledialog, messagebox

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        return [task.description for task in self.tasks]

    def remove_task(self, task):
        self.tasks.remove(task)

class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, (task.priority, task))

    def get_highest_priority_task(self):
        if self.tasks:
            return heapq.heappop(self.tasks)[1]
        else:
            return None

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List GUI")

        self.to_do_list = ToDoList()
        self.priority_queue = PriorityQueue()

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        self.add_button = tk.Button(self.menu_frame, text="Add a Task", command=self.add_task)
        self.add_button.grid(row=0, column=0)

        self.show_button = tk.Button(self.menu_frame, text="Show Next Task", command=self.show_next_task)
        self.show_button.grid(row=0, column=1)

        self.done_button = tk.Button(self.menu_frame, text="Mark Task as Done", command=self.mark_task_as_done)
        self.done_button.grid(row=0, column=2)

        self.next_button = tk.Button(self.menu_frame, text="Show Tasks", command=self.show_tasks)
        self.next_button.grid(row=0, column=3)

        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.root.destroy)
        self.quit_button.grid(row=0, column=4)

    def add_task(self):
        task_description = simpledialog.askstring("Input", "Enter the task description:")
        if task_description:
            priority = simpledialog.askinteger("Input", "Enter task priority (lower value for higher priority):")
            task = Task(task_description, priority)
            self.to_do_list.add_task(task)
            self.priority_queue.add_task(task)

    def show_tasks(self):
        tasks = self.to_do_list.display_tasks()
        task_str = "\n".join(tasks)
        messagebox.showinfo("To-Do List", f"To-Do List:\n{task_str}")

    def show_next_task(self):
        next_task = self.priority_queue.get_highest_priority_task()
        if next_task:
            messagebox.showinfo("Next Task", f"Next Task: {next_task.description}")
        else:
            messagebox.showinfo("Next Task", "No tasks in the priority queue.")

    def mark_task_as_done(self):
        if self.priority_queue.tasks:
            done_task = self.priority_queue.get_highest_priority_task()
            self.to_do_list.remove_task(done_task)
            messagebox.showinfo("Task Completed", f"Task Completed: {done_task.description}")
            self.show_next_task()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


