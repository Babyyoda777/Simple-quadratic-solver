import cmath
import Tkinter
top = Tkinter.Tk()
top.title("Quadratic solver")
top.geometry("600x400")

a = Tkinter.IntVar()
b = Tkinter.IntVar()
c = Tkinter.IntVar()

aentry = Tkinter.Entry(top,textvariable = a, font=('calibre',10,'normal'))
bentry = Tkinter.Entry(top,textvariable = b, font=('calibre',10,'normal'))
centry = Tkinter.Entry(top,textvariable = c, font=('calibre',10,'normal'))

aentry.grid(row=0, column=0)
bentry.grid(row=1, column=0)
centry.grid(row=2, column=0)            

top.mainloop()

#a = input("What is the a value: ")
#b = input("What is the b value: ")
#c = input("What is the c value: ")

# calculate the discriminant
#d = (b**2) - (4*a*c)

# find two solutions
#sol1 = (-b-cmath.sqrt(d))/(2*a)
#sol2 = (-b+cmath.sqrt(d))/(2*a)

#print('The solution are {0} and {1}'.format(sol1,sol2))





