import tkinter as tk
from countdown import CountdownTimer


class CountdownDisplay(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Countdown Timer")
        self.geometry("400x300")
        self.configure(bg="#1e1e1e")

        self.timer = CountdownTimer()
        self.sequence = []
        self.index = 0
        self.running = False

        # Big number display
        self.number_label = tk.Label(
            self, text="--", font=("Helvetica", 96, "bold"),
            fg="#00ff88", bg="#1e1e1e"
        )
        self.number_label.pack(expand=True)

        # Input row
        input_frame = tk.Frame(self, bg="#1e1e1e")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Start from:", fg="white", bg="#1e1e1e").pack(side="left", padx=5)
        self.entry = tk.Entry(input_frame, width=8, justify="center")
        self.entry.insert(0, "10")
        self.entry.pack(side="left", padx=5)

        self.start_button = tk.Button(input_frame, text="Start", command=self.start_countdown)
        self.start_button.pack(side="left", padx=5)


    def start_countdown(self):
        if self.running:
            return
        try:
            n = int(self.entry.get())
        except ValueError:
            self.number_label.config(text="ERR")
            return

        try:
            self.sequence = self.timer.start(n)
        except (TypeError, ValueError) as e:
            self.number_label.config(text="ERR")
            return

        self.index = 0
        self.running = True
        self.tick()



    def tick(self):
        if self.index < len(self.sequence):
            self.number_label.config(text=str(self.sequence[self.index]))
            self.index += 1
            self.after(1000, self.tick)  # 1000ms = 1 second per step
        else:
            self.number_label.config(text="Done!")
            self.running = False


if __name__ == "__main__":
    app = CountdownDisplay()
    app.mainloop()