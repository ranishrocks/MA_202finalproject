#RANISH ABHIJIT JAMODE (202251107) GAURAV JANARDAN BARHATE (202251049) ABBAS MULLA ABDUL TAYYAB HAKIMI (202251002)  PRATIK SINDHIYA (20225103)
import time
from tkinter import *

class TwoBodyView(object):
    def __init__(self):
        self.empty_list = []
        self.read_data()
        self.setup_gui()

    def read_data(self):
        with open("AnalysisResult.txt") as f:
            for line in f:
                x = line.split(",")
                self.empty_list.append(x)

    def setup_gui(self):
        self.tk = Tk()
        self.H = 500
        self.W = 600
        self.canvas = Canvas(self.tk, width=self.W, height=self.H)
        self.tk.title("Graphics")
        self.canvas.pack()
        self.planet_one = self.canvas.create_oval(185, 185, 200, 200, fill="blue")
        self.planet_two = self.canvas.create_oval(285, 285, 300, 300, fill="red")
        self.animate(1)

    def animate(self, i):
        if i < len(self.empty_list):
            self.canvas.move(self.planet_one, (float(self.empty_list[i][0]) - float(self.empty_list[i - 1][0]))*50,
                             (float(self.empty_list[i][1]) - float(self.empty_list[i - 1][1]))*50)
            self.canvas.move(self.planet_two, (float(self.empty_list[i][2]) - float(self.empty_list[i - 1][2]))*50,
                             (float(self.empty_list[i][3]) - float(self.empty_list[i - 1][3]))*50)
            self.canvas.create_line(self.canvas.coords(self.planet_one), fill="blue")
            self.canvas.create_line(self.canvas.coords(self.planet_two), fill="red")
            self.tk.update()
            time.sleep(0.00001)
            self.tk.after(1, self.animate, i + 1)

view = TwoBodyView()
view.tk.mainloop()
