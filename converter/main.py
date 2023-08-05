from tkinter import *

window = Tk()
window.title("Miles to kilo converter")
#window.minsize(width=200, height=100)
window.config(padx=5, pady=5)

def convert():
    new_label = int(input.get()) * 1.60934
    output["text"] = new_label


#entry

input = Entry(width=10)
input.get()
input.grid(row=0, column=1)

#Label1

label1 = Label(text="Miles", font=("Ariel", 15, "bold"))
label1.grid(row=0, column=2)

#Label2

label2 = Label(text="is equal to", font=("Ariel", 15, "bold"))
label2.grid(row=1, column=0)

#output

output = Label(text="0", font=("Ariel", 15, "bold"))
output.grid(row=1, column=1)

#Label3

label3 = Label(text="Km", font=("Ariel", 15, "bold"))
label3.grid(row=1, column=2)

#button

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)







window.mainloop()
