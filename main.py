#!/usr/bin/python3
import tkinter as tk
import gui


def main():
    root = tk.Tk()

    app = gui.EmployeeApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
