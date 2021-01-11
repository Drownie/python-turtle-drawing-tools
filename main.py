from tkinter import *
from tkinter import ttk
from turtle import *
from PIL import Image
from tkinter import messagebox

turtle_box = []
default_title = "Turtle Drawing Tools"

root = Tk()
root.title(default_title)
root.geometry("900x580") # "700x450"
root.configure(bg="gray")
root.resizable(width=False, height=False)

class turtal(object):
	def __init__(self, master):
		self.turt_scr = TurtleScreen(master)
		self.turt = RawTurtle(self.turt_scr)
		self.turt.pendown()
		self.saiz = 10
		self.turt.turtlesize(1+(self.saiz/50))
		self.turt.pensize(1+(self.saiz/20))
		self.dist = 0
		self.rotation = 0
	
	def change(self):
		self.turt.turtlesize(1+(self.saiz/50))
		self.turt.pensize(1+(self.saiz/20))

	def forward(self):
		self.turt.forward(self.dist)

	def rotate(self):
		self.turt.setheading(self.rotation)

def setDistance(s):
	for turt in turtle_box:
		turt.dist = int(s)

def setRotation(rot):
	for turt in turtle_box:
		turt.rotation = int(rot)

def setSize(size):
	for turt in turtle_box:
		turt.saiz = int(size)
		turt.change()

def go():
	for turt in turtle_box:
		turt.rotate()
		turt.forward()

def app():
	col = cEntry.get()
	for tart in turtle_box:
		if col:
			tart.turt.color(col)
		tart.rotate()
		tart.turt.shape(cBox.get())

def save():
	name = nameE.get()
	if name:
		eps = "%s.eps"%name
		png = "%s.png"%name
		root.title(png)
		turtle_box[0].turt.hideturtle()
		monitor.postscript(file=eps)
		img = Image.open(eps)
		img.save(png, "png")
		turtle_box[0].turt.showturtle()
	else:
		messagebox.showerror("Error", "the file need a name")

def Del():
	turtle_box[0].turt.reset()
	root.title(default_title)

monitor = Canvas(root, width=580, height=580, bg="white")
monitor.grid(row=0, rowspan=30, column=0, columnspan=1)

box = Frame(root)
box.grid(row=0, column=1, rowspan=12, columnspan=3)

#### in the frame

distScale = Scale(box, from_=0, to=100, orient=HORIZONTAL, command=setDistance, length=132, label="distance")
distScale.set(0)
distScale.grid(row=0, ipadx=50, column=0, columnspan=2, sticky=W)

movButton = Button(box, text="Move", command=go)
movButton.grid(row=0, column=2, ipadx=10, ipady=10, sticky=W)

rotScale = Scale(box, from_=0, to=360, orient=HORIZONTAL, command=setRotation, length=212, label="rotation")
rotScale.set(0)
rotScale.grid(row=2, ipadx=50, column=0, columnspan=3, sticky=W)

sizScale = Scale(box, from_=5, to=50, orient=HORIZONTAL, command=setSize, length=212, label="size")
sizScale.set(10)
sizScale.grid(row=4, ipadx=50, column=0, columnspan=3, sticky=W)

shpLabel = Label(box, text="Shape : ")
shpLabel.grid(row=6, column=0)

value = ["turtle", "circle", "square", "triangle", "arrow", "classic"]
cBox = ttk.Combobox(box, values=value, font=("Arial", 10), width=20)
cBox.set("classic")
cBox.grid(row=6, column=1)

cLabel = Label(box, text="color : ", font=("Arial", 10))
cLabel.grid(row=8, column=0, sticky=W, ipadx=5)

cEntry = Entry(box, font=("Arial", 10))
cEntry.grid(row=8, column=1, ipadx=10, sticky=W)

appButton = Button(box, text="Apply", command=app)
appButton.grid(row=6, column=2, ipadx=5, sticky=W, rowspan=3, ipady=10)

delButton = Button(box, text="Delete", fg="red", command=Del)
delButton.grid(row=10, rowspan=2, columnspan=3, ipadx=117, ipady=5)

nameE = Entry(box, font=("Arial", 10), width=32)
nameE.grid(row=12, column=0, columnspan=2)

saveButton = Button(box, text="Save", command=save)
saveButton.grid(row=12, column=2, ipadx=8, sticky=W)

one = turtal(monitor)
turtle_box.append(one)
root.mainloop()