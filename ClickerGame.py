# Basically a clicking game.
from tkinter import *

count = 0

def clickstier4():
    global count
    count += 1
    guiClickText.config(text=f" Clicks: {count} ")
    if count >= 50:
        guiButton.config(command=clickstier3,
                         fg="#dbca2e", bg="#c7341a",
                         activebackground="#c7651a", activeforeground="#dbca2e")
        guiTextMisc.config(text="50 clicks = Rookie ✅\n200 clicks = Pro\n500 clicks = Skilled\n1000 clicks = Supernatural ",
                            font=('Monospace', 15, 'italic'))


def clickstier3():
    global count
    count += 2
    guiClickText.config(text=f" Clicks: {count} ")
    if count >= 200:
        guiButton.config(command=clickstier2,
                         fg="#eaf6ff", bg="#1a75c7",
                         activebackground="#3ba9f4", activeforeground="#003e80")
        guiTextMisc.config(
            text="50 clicks = Rookie ✅\n200 clicks = Pro ✅\n500 clicks = Skilled\n1000 clicks = Supernatural ",
            font=('Monospace', 15, 'italic'))


def clickstier2():
    global count
    count += 5
    guiClickText.config(text=f" Clicks: {count} ")
    if count >= 500:
        guiButton.config(command=clickstier1,
                         fg="#fff200", bg="#ff4d00",
                         activebackground="#ff944d", activeforeground="#0a0a0a")
        guiTextMisc.config(
            text="50 clicks = Rookie ✅\n200 clicks = Pro ✅\n500 clicks = Skilled ✅\n1000 clicks = Supernatural ",
            font=('Monospace', 15, 'italic'))


def clickstier1():
    global count
    count += 10
    guiClickText.config(text=f" Clicks: {count} ")

    # Show mastery message once when Tier 1 unlocks
    if count >= 1000:
        guiTextMisc.config(
            text="50 clicks = Rookie ✅\n200 clicks = Pro ✅\n500 clicks = Skilled ✅\n1000 clicks = Supernatural ✅ ",
            font=('Monospace', 15, 'italic'))
        masterLabel = Label(gui,
                            text="YOU'VE MASTERED THE GAME!\nGame by: Imperfexion!",
                            font=('Helvetica', 18, 'bold'),
                            fg="#00ffcc",
                            bg="#1a1a1a",
                            relief=RAISED,
                            bd=5,
                            padx=10,
                            pady=5)
        masterLabel.pack(pady=10)

        # Disable the button after 1000 clicks
        guiButton.config(state=DISABLED)


# Setup GUI
gui = Tk()
gui.config(bg="#0299e5")
gui.geometry("550x550")
gui.title("Clicker thingy")

# Icon (optional, make sure path is correct)
icon = PhotoImage(file="C:\\Users\\imper\\OneDrive\\Images\\0cpsRESIZED.png")
gui.iconphoto(gui, icon)

# Labels and button
guiText = Label(gui,
                text="Welcome to a clicker game",
                font=('Monospace', 20, 'bold'),
                fg="#4d7ef0",
                bg='#13254f',
                relief=RAISED,
                bd=10,
                padx=10,
                pady=5,
                image=icon,
                compound='right')
guiClickText = Label(gui,
                     text=f" Clicks: {count} ",
                     font=('Arial', 20, 'bold'),
                     relief=RAISED,
                     bd=3,
                     fg="#fcc603",
                     bg="#205391")

guiButton = Button(gui,
                   text="Click me!",
                   font=("Verdana", 30, 'bold'),
                   command=clickstier4,
                   relief=RAISED,
                   bd=7,
                   fg="#FFFFFF",
                   bg="#000000",
                   activebackground="#FFFFFF",
                   activeforeground="#000000")
guiTextMisc = Label(gui, text="50 clicks = Rookie\n200 clicks = Pro\n500 clicks = Skilled\n1000 clicks = Supernatural ",
                    font=('Monospace', 15, 'italic'), fg="yellow", bg="black", relief=RAISED, bd=5, padx=5, pady=5)

# Pack Widgets.
guiText.pack(pady=10)         # Title label at the top
guiClickText.pack(padx=10, pady=10)    # Click counter in the middle
guiButton.pack()       # Button at the bottom
guiTextMisc.pack(padx=5, pady=10)

gui.mainloop()