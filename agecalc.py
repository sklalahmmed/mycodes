import tkinter as tk
from PIL import Image,ImageTk
window=tk.Tk()
window.geametry("620*780")
window.title("Age calc")
name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date = tk.Label(text = "Day")
date.grid(column=0,row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)

def getInput():
    name=nameEntry.get()
    monkey = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get()))

    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = "Hey {monkey}!!!. you are {age} years old!!!".format(mokey=name, age=monkey.age())
    textArea.insert(tk.END,answer)

button = tk.Button(window,text="Calculate Age",command=getInput,bg="pink")
button.grid(column=1,row=5)

class person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

image=Image.open('app_image.jpeg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lable_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)
window.mainloop()
