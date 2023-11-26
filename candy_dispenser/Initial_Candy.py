import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

counter = 0

class Stack:
    def __init__(self, canvas):
        self.canvas = canvas
        self.rectangle_stack = []
        self.colors = []
        self.spring_offset = 20
        self.spring_height = 450
        self.spring_width = 300
        self.predefined_colors = ["red", "green", "blue", "yellow", "orange"]

    def push(self):
        if len(self.rectangle_stack) <= 15:
            global counter
            if counter <= 15:
                adjust_label_position(20)
                counter += 1
            rect_x1 = 50
            rect_x2 = 250
            rect_height = 30

            if self.rectangle_stack:
                rect_y2 = self.rectangle_stack[0][3]
                rect_y1 = rect_y2 - self.spring_offset
            else:
                rect_y2 = upper_y
                rect_y1 = rect_y2 - rect_height

            for i in range(len(self.rectangle_stack)):
                self.canvas.move(self.rectangle_stack[i][4], 0, self.spring_offset)

            color = self.predefined_colors[counter % len(self.predefined_colors)]
            self.colors.insert(0, color)

            rect = self.canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline='black', fill=color, tags='rect')
            self.rectangle_stack.insert(0, (rect_x1, rect_y1, rect_x2, rect_y2, rect))

    def pop(self):
        if self.rectangle_stack:
            global counter
            if counter != 0:
                adjust_label_position(-self.spring_offset)
                counter -= 1
            rect_coords = self.rectangle_stack.pop(0)
            self.canvas.delete(rect_coords[4])

            popped_color = self.colors.pop(0)
            messagebox.showinfo("Popped Candy", f"Popped candy color: {popped_color}")

            for i in range(len(self.rectangle_stack)):
                self.canvas.move(self.rectangle_stack[i][4], 0, -self.spring_offset)
        else:
            messagebox.showwarning("Empty", "Candy Dispenser is Empty")

    def is_empty(self):
        if len(self.rectangle_stack):
            messagebox.showwarning("Message", "True")
        else:
            messagebox.showinfo("Message", "False")
            return len(self.rectangle_stack) == 0
        

    def top_candy(self):
        if self.rectangle_stack:
            messagebox.showinfo("Top Candy", f"Top candy color: {self.colors[0]}")
        else:
            messagebox.showwarning("Empty", "Candy Dispenser is Empty")
            
    def length(self):
        return len(self.rectangle_stack)


def adjust_label_position(delta_height):
    global upper_y
    upper_y += delta_height
    new_height = fixed_bottom - upper_y
    my_label.place(x=50, y=upper_y)
    resized = my_pic.resize((200, new_height), Image.LANCZOS)
    new_pic = ImageTk.PhotoImage(resized)
    my_label.config(image=new_pic)
    my_label.image = new_pic


root = Tk()
root.title("Candy Dispenser")
root.geometry("600x600")

canvas = Canvas(root, width=600, height=600, bg="white")
canvas.pack()

rectangleStack = Stack(canvas)

canvas.create_rectangle(50, 150, 250, 500, fill="grey")

my_pic = Image.open("./spring.png")
resized = my_pic.resize((200, 330), Image.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)

fixed_bottom = 600
upper_y = fixed_bottom - new_pic.height()
my_label = Label(canvas, image=new_pic, bg="grey")
my_label.place(x=50, y=upper_y)

Push_btn = Button(canvas, text="Push", command=rectangleStack.push)
Pop_btn = Button(canvas, text="Pop", command=rectangleStack.pop)
TopCandy_btn = Button(canvas, text="Top Candy", command=rectangleStack.top_candy)
IsEmpty_btn = Button(canvas, text="Is_Empty", command=rectangleStack.is_empty)
Length_btn = Button(canvas, text="Length", command=lambda: messagebox.showinfo("Length", f"Number of candies: {rectangleStack.length()}"))

canvas.create_window(400, 400, window=Push_btn)
canvas.create_window(400, 450, window=Pop_btn)
canvas.create_window(500, 400, window=TopCandy_btn)
canvas.create_window(500, 450, window=IsEmpty_btn)
canvas.create_window(450, 500, window=Length_btn)

root.mainloop()
