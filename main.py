import random
import tkinter as tk

def generate_card_numbers():
    numbers = [random.randint(1, 9) for _ in range(16)]
    return numbers

def generate_card():
    card_numbers = generate_card_numbers()
    data_label.config(text="Card Numbers: {}".format("".join(map(str, card_numbers))))

def close_window(window):
    window.destroy()

# Create the main application window
window = tk.Tk()
window.title("Software App Panel")
window.geometry("400x300")

# Create a label to display the generated data
data_label = tk.Label(window, text="Welcome to the Dashboard!", wraplength=350)
data_label.pack(pady=20)

# Create Button 1
def open_gift_card_generator_window():
    gift_card_generator_window = tk.Toplevel(window)
    gift_card_generator_window.title("Gift Card Generator")
    gift_card_generator_window.geometry("300x200")

    generate_card_label = tk.Label(gift_card_generator_window, text="Click the button to generate 16 numbers between 1 and 9")
    generate_card_label.pack(pady=20)

    generate_card_button = tk.Button(gift_card_generator_window, text="Generate Card", command=generate_card)
    generate_card_button.pack()

    back_button = tk.Button(gift_card_generator_window, text="Back", command=lambda: close_window(gift_card_generator_window))
    back_button.pack(pady=10)

button1 = tk.Button(window, text="Gift Card Generator", command=open_gift_card_generator_window)
button1.pack()

# Start the Tkinter event loop
window.mainloop()
