from tkinter import *

# Define window size
window_width = 800
window_height = 800

# Create the main window
window = Tk()
window.title("Fati Player 🎥")

# Set window size
window.geometry(f"{window_width}x{window_height}")

# Create a label for the text entry field
text_label = Label(window, text="Enter text here:", bg="#AAAAAA")
text_label.pack(pady=10)

# Create the text entry field
text_entry = Entry(window, width=50)
text_entry.pack(pady=10)

# Define a function to handle button click (placeholder for now)
def button_click():
    # This function can be used to perform an action when the button is clicked
    print("Button clicked!")
    print(text_entry.get())
    # Add your desired functionality here

# Create the button
button = Button(window, text="Click Me!", command=button_click)
button.pack(pady=10)

# Run the main event loop
window.mainloop()
