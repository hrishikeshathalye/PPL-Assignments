import os
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename, askopenfilename
from PIL import ImageTk, Image
bgColor = "white"

class Paint(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("Paint Application")

        #Top Bar
        self.brush_button = Button(self.root, text='Brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=4)

        self.color_button = Button(self.root, text='Brush Color', command=self.choose_color)
        self.color_button.grid(row=0, column=5)

        self.chgbg_button = Button(self.root, text='Background Color', command=self.choose_bgcolor)
        self.chgbg_button.grid(row=0, column=6)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=7)

        self.choose_size_button = Scale(self.root, from_=1, to=100, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=8)

        self.reset_button = Button(self.root, text='Reset', command=self.reset_canvas)
        self.reset_button.grid(row=0, column=9)

        self.c = Canvas(self.root, bg='white', width=1200, height=700, bd = 10)
        self.c.grid(row=2, column = 4, columnspan=9, rowspan = 7)

        self.menubar = Menu(self.root)  
        self.menubar.add_command(label="Load Image", command = self.load_img)  
        self.menubar.add_command(label="Save Image", command = self.save_img)
        self.root.config(menu = self.menubar)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = "black"    #default color
        self.eraser_on = False
        self.active_button = self.brush_button
        self.active_button.config(relief=RAISED)
        self.active_button.config(relief=SUNKEN)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def choose_bgcolor(self):
        global bgColor
        bgColor = askcolor(color=self.color)[1]
        self.c.configure(bg = bgColor)

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None
    
    def reset_canvas(self):
        self.c.delete("all")
        self.c.configure(bg = "white")

    #image loading functionality
    def load_img(self):
        self.filename = askopenfilename()
        self.img = Image.open(self.filename)
        self.c.image = ImageTk.PhotoImage(self.img)
        self.c.create_image(0,0, image = self.c.image, anchor = 'nw')

    #image saving functionality    
    def save_img(self):
        fileName = asksaveasfilename()
        self.c.postscript(file = fileName + '.eps') 
        img = Image.open(fileName + '.eps') 
        img.save(fileName + '.png', 'png')
        os.remove(fileName + '.eps')

if __name__ == '__main__':
    Paint()