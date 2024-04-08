from tkinter import Tk, Button, Label, Text, W
from PIL import Image, ImageTk


BACKGROUND_COLOR = "#000000"
seg = 5
WRITING = True  


def countdown():
    global WRITING, seg
    if seg >=0 :
        time_left.config(text=seg)  
        seg -= 1  
        window.after(1000, countdown)
    else :
        WRITING  = True
        finish_type()

def finish_type():
    words = len(input_text.get("1.0", "end-1c").split())
    time_left.config(text=f'You time has ended. You\'ve written {words} words')
    input_text.delete("1.0", "end")
    reset_time()

def reset_time():
    global seg, WRITING
    seg = 5

def typing(event=None):
    global WRITING
    if WRITING:
        WRITING = False
        countdown()
    else :
        reset_time()
        

window = Tk()
window.title('Most Dangerous Python Writer')
window.minsize(height=620, width=1100)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

welcome = Label(text='Welcome to Most Dangerous Python Writer', font=('Arial', 24, 'bold'), background=BACKGROUND_COLOR, fg='#fafafa')
welcome.grid(row=1, column=1, padx=150, pady=(20))

label = Label(text='Dont\'t Stop Writing', font=('Arial', 18, 'normal'), background=BACKGROUND_COLOR, fg='#fafafa')
label.grid(row=2, column=1, padx=150, pady=(0,20))

input_text = Text(window, height=7, width=40, wrap="word", font=('arial', 20, 'bold'), bd=6,)
input_text.grid(column=1, row=3)
input_text.focus()


time_left = Label(text='', font=('Arial', 20, 'normal'), background=BACKGROUND_COLOR, fg='#fafafa')
time_left.grid(column=1, row=4, pady=10)

window.bind('<Key>', typing )


window.mainloop()