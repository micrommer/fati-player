from tkinter import *
root = Tk()
root.title('Account Player')
root.geometry('895x500+200+200')
root.configure(bg="#fff")
root.resizable(False, False)
img = PhotoImage(file='login0.png')
img1 = PhotoImage(file='user.png')
root.iconphoto(False, img1)
Label(root, image=img, bg="#fff").place(x=5, y=5)
frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)
heading = Label(frame, text='Sign in', fg='#a30349', bg='white', font=('Microsoft YaHei Light', 30, 'bold'))
###############################################################################################################
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
Frame(frame, width=300, height=3, bg='purple').place(x=25, y=107)
################################################################################################################
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')

Frame(frame, width=300, height=3, bg='purple').place(x=25, y=177)
#############################################################################################################
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0).place(x=35, y=204)
label = Label(frame, text='Dont have an account?', fg='black', bg='white', font=('Microsoft YaHei Light', 9))
label.place(x=75, y=175)

root.mainloop()