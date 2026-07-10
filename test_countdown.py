import unittest
import tkinter as tk
from countdown import CountdownTimer
from countdown_display import CountdownDisplay

class TestCountdownTimer(unittest.TestCase):

    # Cycle 1 - Float Input
    def test_float_input_raises_error(self):
        timer = CountdownTimer()
        with self.assertRaises(TypeError):
            timer.start(3.7)

    # Cycle 2 - Very Large Number
    def test_large_number_countdown(self):
        timer = CountdownTimer()
        result = timer.start(1000000)
        self.assertEqual(result[0], 1000000)   # starts at 1000000
        self.assertEqual(result[-1], 0)        # ends at 0
        self.assertEqual(len(result), 1000001) # correct length

    # Cycle 3 - Negative Number
    def test_negative_number_raises_value_error(self):
        timer = CountdownTimer()
        with self.assertRaises(ValueError):
            timer.start(-5)

    # Cycle 4 - NaN input (non-digit characters)
    def test_invalid_input_shows_error(self):
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(0, "not_a_number")

        self.app.start_countdown()

        self.assertEqual(self.app.number_label.cget("text"), "ERR")
        self.assertFalse(self.app.running)

    # Cycle 5 - Zero Input
    def test_zero_input_completes_instantly(self):
        self.app = CountdownDisplay() 
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(0, "0")
        self.app.start_countdown()
        
        # It should immediately process the single-element sequence [0]
        self.assertEqual(self.app.sequence, [0])
        self.assertEqual(self.app.number_label.cget("text"), "0")


if __name__ == "__main__":
    unittest.main()
