import tkinter as tk
from tkinter import ttk
from trigo_sin_cos_tan import sine_power_series, cosine_power_series

class TrigCalcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Trigonometric Calculator")

        # Create input frame
        input_frame = ttk.LabelFrame(root, text="Input")
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Angle input
        ttk.Label(input_frame, text="Angle:").grid(row=0, column=0, padx=5, pady=5)
        self.angle_var = tk.StringVar()
        self.angle_entry = ttk.Entry(input_frame, textvariable=self.angle_var)
        self.angle_entry.grid(row=0, column=1, padx=5, pady=5)

        # Calculate button
        ttk.Button(input_frame, text="Calculate", command=self.calculate).grid(row=1, column=0, columnspan=2, pady=10)

        # Results frame
        results_frame = ttk.LabelFrame(root, text="Results")
        results_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.result_text = tk.Text(results_frame, height=5, width=40)
        self.result_text.grid(row=0, column=0, padx=5, pady=5)

    def calculate(self):
        try:
            angle = float(self.angle_var.get())
            sin_result = sine_power_series(angle, 10)
            cos_result = cosine_power_series(angle, 10)

            result = f"Sine: {sin_result}\nCosine: {cos_result}"
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter a valid number")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrigCalcGUI(root)
    root.mainloop()