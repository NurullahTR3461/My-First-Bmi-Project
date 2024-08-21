
import tkinter
import messagebox

window = tkinter.Tk()
window.title("My Simple Bmı Calculator")
window.minsize(width=500,height=500)



def Click_button_1():
    weight = my_entry_1.get()
    height = my_entry_2.get()

    if weight == "" or height == "":
        messagebox.showinfo("Erors","Please Enter both of them")
    else:
        try:
            my_bmi = float(weight) / (float(height)/100)**2
            my_bmi_outcome.config(text=f"your bmi is : {my_bmi}")
        except:
            messagebox.showinfo("Errors","Please valid values")

    def message_function():
        Weight = my_entry_1.get()
        height = my_entry_2.get()
    bmi =float(weight) / (float(height) / 100) ** 2

    if bmi < 16:
        messagebox.showinfo("Sever Thinness", "You need to put on weight")
    elif bmi <18.5:
        messagebox.showinfo("Mild Thinness","you need to put on weight")
    elif (bmi > 18.5) and (bmi <=24.9):
        messagebox.showinfo("Normal","you need to protect your weight")
    elif (bmi > 24.9) and (bmi <= 29.9):
        messagebox.showinfo("Overweight","you need to lose your weight")
    elif bmi < 35.5:
        messagebox.showinfo("Overweight","you need to lose your  weight")
    elif bmi <= 40:
        messagebox.showinfo("Obese Class 2 ","you need to go to doctor for your health")





my_label_1 = tkinter.Label(text="Enter your weight(kg)")
my_label_1.pack()


my_entry_1 = tkinter.Entry()
my_entry_1.pack()



my_label_2 = tkinter.Label(text="Enter your height(cm)")
my_label_2.pack()

my_entry_2 = tkinter.Entry()
my_entry_2.pack()



my_button =tkinter.Button(text="calculate",command=Click_button_1)
my_button.pack()



my_bmi_outcome = tkinter.Label()
my_bmi_outcome.pack()

window.mainloop()



