#!/usr/bin/env python3
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.draw_grid()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side = "right")

        #self.quit = tk.Button(self, text="QUIT", fg="red",
        #                      command=self.master.destroy)
        #self.quit.pack()

    def say_hi(self):
        print("hi there, everyone!")

    def draw_grid(self):
    	self.myCanvas = tk.Canvas(self)
    	self.myCanvas.configure(width = 260, height = 260, bg = "green")
    	self.myCanvas.pack(padx = 10, pady = 20, side = "left")
    	self.myCanvas.create_line(5, 5, 255, 5, width = 2)
    	self.myCanvas.create_line(5, 30, 255, 30, width = 2)
    	for row in range(10):
    		print("maika ti ")
    		self.myCanvas.create_line(5, 55, 255, 55, width = 2)
    	#for column in range(0,10):
 		

#create tk instance
root = tk.Tk()
#create application instance
app = Application(master=root)
#set windows title
app.master.title("My Do-Nothing Application")
#set windows size
app.master.maxsize(500, 500)
app.master.minsize(300, 300)
#runs main loop
app.mainloop()