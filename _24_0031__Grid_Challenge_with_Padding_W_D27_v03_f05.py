from tkinter import *

window = Tk()
window.title("This is the title for the Window name!!!")
window.minsize(width=500, height=300)
#If you want to pad the entire window as a whole, use the below code:
window.config(padx=50, pady=50)

# Labels
label = Label(text="This is old text")
label.config(text="Label")
label.grid(column=0, row=0)
#IF you ONLY want to have padding around 1 SPECIFIC widget, then apply the .config(padx= , pady= ) to just that widget block of code.
label.config(padx=50, pady=50)

# Buttons
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

button = Button(text="Button")
button.grid(column=1, row=1)

# Create an Entry widget
entry = Entry(width=16)
entry.grid(column=3, row=2)

# Set default text or placeholder
entry.insert(0, "Entry text as Placeholder")

# completes window loop to remain open:
window.mainloop()