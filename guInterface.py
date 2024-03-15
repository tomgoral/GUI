import tkinter 

if __name__ == "__main__":
    window = tkinter.Tk()

    def buttonEvent():
        # capture input from a text box
        print(textBox.get())

    window.title("My first app")
    window.geometry("400x400")

    frame=tkinter.Frame(window)
    frame.pack()

    label = tkinter.Label(frame, text="Hello World")
    label.pack() 

    button = tkinter.Button(frame, text="Click me!", command=buttonEvent)
    button.pack()

    textBox = tkinter.Entry(frame)
    textBox.pack()

    window.mainloop()