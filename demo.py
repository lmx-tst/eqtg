from tkinter import Tk, Entry, Button, StringVar

class App:
    def __init__(self, statWindow):
        statWindow.title("View Statistics")
        statWindow.config(bg = "grey")
        statWindow.geometry('800x900')

        self.searched = StringVar()
        searchBox = Entry(statWindow, textvariable=self.searched)
        searchBox.place(x= 450, y=50, width = 200, height = 24)
        enterButton = Button(statWindow, text ="Enter", command=self.searchButton)
        enterButton.config(height = 1, width = 4)
        enterButton.place(x=652, y=50)

    def searchButton(self):
        text = self.searched.get()
        print(text)


root = Tk()
app = App(root)
root.mainloop()