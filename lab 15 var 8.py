import json
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore

def load_data():
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'input.json' not found.")
        return {}

def show_histogram():
    data = load_data()
    if data:
        months = list(data.keys())
        sales = list(data.values())

        fig, ax = plt.subplots()
        ax.bar(months, sales)
        ax.set_title("Sales by Month")
        ax.set_xlabel("Month")
        ax.set_ylabel("Sales")

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().place(x=50, y=50, width=350, height=200)

window = tk.Tk()
window.title("Sales Histogram")
window.geometry("450x300")
window.configure(bg="brown")

show_histogram_button = tk.Button(window, text="Show Histogram", command=show_histogram)
show_histogram_button.place(x=175, y=10)

window.mainloop()
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        numbers = list(map(float, entry.get().split()))
        total_sum = sum(numbers)
        avg = total_sum / len(numbers) if numbers else 0
        result_text.set(f"Sum: {total_sum}, Average: {avg}")
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers separated by spaces.")

window = tk.Tk()
window.title("Array Sum and Average Calculator")
window.geometry("400x200")

frame = tk.Frame(window)
frame.pack(pady=20)

entry = tk.Entry(frame, width=30)
entry.pack()

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack()

window.mainloop()
