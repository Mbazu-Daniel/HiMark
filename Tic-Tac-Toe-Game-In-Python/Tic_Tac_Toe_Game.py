from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = Tk()
root.title("Tic Tac Toe")
# add Buttons
build1 = ttk.Button(root, text=" ")
build1.grid(row=0, column=0, sticky="snew", ipadx=40, ipady=40)
build1.config(command=lambda: ButtonClick(1))

build2 = ttk.Button(root, text=" ")
build2.grid(row=0, column=1, sticky="snew", ipadx=40, ipady=40)
build2.config(command=lambda: ButtonClick(2))

build3 = ttk.Button(root, text=" ")
build3.grid(row=0, column=2, sticky="snew", ipadx=40, ipady=40)
build3.config(command=lambda: ButtonClick(3))

build4 = ttk.Button(root, text=" ")
build4.grid(row=1, column=0, sticky="snew", ipadx=40, ipady=40)
build4.config(command=lambda: ButtonClick(4))

build5 = ttk.Button(root, text=" ")
build5.grid(row=1, column=1, sticky="snew", ipadx=40, ipady=40)
build5.config(command=lambda: ButtonClick(5))

build6 = ttk.Button(root, text=" ")
build6.grid(row=1, column=2, sticky="snew", ipadx=40, ipady=40)
build6.config(command=lambda: ButtonClick(6))

build7 = ttk.Button(root, text=" ")
build7.grid(row=2, column=0, sticky="snew", ipadx=40, ipady=40)
build7.config(command=lambda: ButtonClick(7))

build8 = ttk.Button(root, text=" ")
build8.grid(row=2, column=1, sticky="snew", ipadx=40, ipady=40)
build8.config(command=lambda: ButtonClick(8))

build9 = ttk.Button(root, text=" ")
build9.grid(row=2, column=2, sticky="snew", ipadx=40, ipady=40)
build9.config(command=lambda: ButtonClick(9))

playerturn = ttk.Label(root, text="   Player 1 turn!  ")
playerturn.grid(row=3, column=0, sticky="snew", ipadx=40, ipady=40)

playerdetails = ttk.Label(root, text="    Player 1 is X\n\n    Player 2 is O")
playerdetails.grid(row=3, column=2, sticky="snew", ipadx=40, ipady=40)

res = ttk.Button(root, text="Restart")
res.grid(row=3, column=1, sticky="snew", ipadx=40, ipady=40)
res.config(command=lambda: restartbutton())

a = 1
b = 0
c = 0


def restartbutton():
    global a, b, c
    a = 1
    b = 0
    c = 0
    playerturn["text"] = "   Player 1 turn!   "
    build1["text"] = " "
    build2["text"] = " "
    build3["text"] = " "
    build4["text"] = " "
    build5["text"] = " "
    build6["text"] = " "
    build7["text"] = " "
    build8["text"] = " "
    build9["text"] = " "
    build1.state(["!disabled"])
    build2.state(["!disabled"])
    build3.state(["!disabled"])
    build4.state(["!disabled"])
    build5.state(["!disabled"])
    build6.state(["!disabled"])
    build7.state(["!disabled"])
    build8.state(["!disabled"])
    build9.state(["!disabled"])


# after getting result(win or loss or draw) disable button
def disableButton():
    build1.state(["disabled"])
    build2.state(["disabled"])
    build3.state(["disabled"])
    build4.state(["disabled"])
    build5.state(["disabled"])
    build6.state(["disabled"])
    build7.state(["disabled"])
    build8.state(["disabled"])
    build9.state(["disabled"])


def ButtonClick(id):
    global a, b, c
    print("ID:{}".format(id))

    # for player 1 turn
    if id == 1 and build1["text"] == " " and a == 1:
        build1["text"] = "X"
        a = 0
        b += 1
    if id == 2 and build2["text"] == " " and a == 1:
        build2["text"] = "X"
        a = 0
        b += 1
    if id == 3 and build3["text"] == " " and a == 1:
        build3["text"] = "X"
        a = 0
        b += 1
    if id == 4 and build4["text"] == " " and a == 1:
        build4["text"] = "X"
        a = 0
        b += 1
    if id == 5 and build5["text"] == " " and a == 1:
        build5["text"] = "X"
        a = 0
        b += 1
    if id == 6 and build6["text"] == " " and a == 1:
        build6["text"] = "X"
        a = 0
        b += 1
    if id == 7 and build7["text"] == " " and a == 1:
        build7["text"] = "X"
        a = 0
        b += 1
    if id == 8 and build8["text"] == " " and a == 1:
        build8["text"] = "X"
        a = 0
        b += 1
    if id == 9 and build9["text"] == " " and a == 1:
        build9["text"] = "X"
        a = 0
        b += 1
    # for player 2 turn
    if id == 1 and build1["text"] == " " and a == 0:
        build1["text"] = "O"
        a = 1
        b += 1
    if id == 2 and build2["text"] == " " and a == 0:
        build2["text"] = "O"
        a = 1
        b += 1
    if id == 3 and build3["text"] == " " and a == 0:
        build3["text"] = "O"
        a = 1
        b += 1
    if id == 4 and build4["text"] == " " and a == 0:
        build4["text"] = "O"
        a = 1
        b += 1
    if id == 5 and build5["text"] == " " and a == 0:
        build5["text"] = "O"
        a = 1
        b += 1
    if id == 6 and build6["text"] == " " and a == 0:
        build6["text"] = "O"
        a = 1
        b += 1
    if id == 7 and build7["text"] == " " and a == 0:
        build7["text"] = "O"
        a = 1
        b += 1
    if id == 8 and build8["text"] == " " and a == 0:
        build8["text"] = "O"
        a = 1
        b += 1
    if id == 9 and build9["text"] == " " and a == 0:
        build9["text"] = "O"
        a = 1
        b += 1

    # checking for winner
    if (
        build1["text"] == "X"
        and build2["text"] == "X"
        and build3["text"] == "X"
        or build4["text"] == "X"
        and build5["text"] == "X"
        and build6["text"] == "X"
        or build7["text"] == "X"
        and build8["text"] == "X"
        and build9["text"] == "X"
        or build1["text"] == "X"
        and build4["text"] == "X"
        and build7["text"] == "X"
        or build2["text"] == "X"
        and build5["text"] == "X"
        and build8["text"] == "X"
        or build3["text"] == "X"
        and build6["text"] == "X"
        and build9["text"] == "X"
        or build1["text"] == "X"
        and build5["text"] == "X"
        and build9["text"] == "X"
        or build3["text"] == "X"
        and build5["text"] == "X"
        and build7["text"] == "X"
    ):
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is player 1")
    elif (
        build1["text"] == "O"
        and build2["text"] == "O"
        and build3["text"] == "O"
        or build4["text"] == "O"
        and build5["text"] == "O"
        and build6["text"] == "O"
        or build7["text"] == "O"
        and build8["text"] == "O"
        and build9["text"] == "O"
        or build1["text"] == "O"
        and build4["text"] == "O"
        and build7["text"] == "O"
        or build2["text"] == "O"
        and build5["text"] == "O"
        and build8["text"] == "O"
        or build3["text"] == "O"
        and build6["text"] == "O"
        and build9["text"] == "O"
        or build1["text"] == "O"
        and build5["text"] == "O"
        and build9["text"] == "O"
        or build3["text"] == "O"
        and build5["text"] == "O"
        and build7["text"] == "O"
    ):
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is player 2")
    elif b == 9:
        disableButton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")

    if a == 1 and c == 0:
        playerturn["text"] = "   Player 1 turn!   "
    elif a == 0 and c == 0:
        playerturn["text"] = "   Player 2 turn!   "


root.mainloop()
