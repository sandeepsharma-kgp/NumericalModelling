import tkinter as tk
from tkinter import ttk
from tkinter import *
import sys
import matplotlib.pyplot as plt
import matplotlib
import math
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
matplotlib.use('TkAgg')
style.use('ggplot')
FONT = ('verdana', 12)
subsidence = {}
sub1111 = []
x1111 = []
y1111 = []
dxy1111 = []
dx1111 = []
dy1111 = []
str1111 = []
list_x = []
list_y = []
list_a = []
list_b = []

global x, y, a, b, i, j, Gallery_width, Pillar_width, no_of__row, no_of__column, Depth, Seam_thickness, Angle,\
    Numbers_not_extracted, grid_row, grid_column
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def frome(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def influence_area(depth, length, breadth, draw, thickness, grid_row, grid_column):
    global subsidence
    global x1111, y1111, sub1111, dxy1111, dx1111, dy1111, str1111

    influence = depth * math.tan(math.radians(draw))
    influence_length = length + 2 * influence
    influence_breadth = breadth + 2 * influence
    point = points(influence_length, influence_breadth, grid_row, grid_column)
    influence_points = influence_point(point, influence)
    subsidence = Subsidence(influence_points, length, breadth, influence, thickness)
    dxy1 = []
    dx1 = []
    dy1 = []

    '''for x11,y11,x111,y111,sub in zip(subsidence['x11'],subsidence['y11'],subsidence['x111'],subsidence['y111'],subsidence['sub']):
        dist=math.sqrt((x111-x11)**2+(y111-y11)**2)
        tanAlpha=dist/depth
        dxy1.append(sub*tanAlpha)'''

    for x11, y11, x111, y111, sub in zip(subsidence['x11'], subsidence['y11'], subsidence['x111'], subsidence['y111'],
                                         subsidence['sub']):
        tanalpha = math.sqrt(
            ((x111 - (influence + 0.5 * breadth)) ** 2 + (y111 - (influence + 0.5 * length)) ** 2)) / depth
        dxy1.append(sub * tanalpha)
        beta = math.acos((x111 - (influence + 0.5 * breadth)) / (math.sqrt((x111 - (influence + 0.5 * breadth)) ** 2 + (y111 - (influence + 0.5 * length)) ** 2)))
        beta1 = math.acos((y111 - (influence + 0.5 * length)) / (math.sqrt((x111 - (influence + 0.5 * breadth)) ** 2 + (y111 - (influence + 0.5 * length)) ** 2)))
        dx1.append(sub * tanalpha * math.cos(beta))
        dy1.append(sub * tanalpha * math.cos(beta1))

    subsidence['dxy'] = dxy1
    subsidence['dx'] = dx1
    subsidence['dy'] = dy1

    df = pd.DataFrame(subsidence)

    for c, d in point:
        z = df['sub'][(df['x11'] == c) & (df['y11'] == d)]
        dxy = df['dxy'][(df['x11'] == c) & (df['y11'] == d)]
        dx = df['dx'][(df['x11'] == c) & (df['y11'] == d)]
        dy = df['dy'][(df['x11'] == c) & (df['y11'] == d)]
        sub1111.append(depth + z.sum())
        x1111.append(c)
        y1111.append(d)
        dxy1111.append(dxy.sum())
        dx1111.append(dx.sum())
        dy1111.append(dy.sum())
    st = {}
    st['x22'] = x1111
    st['y22'] = y1111
    st['s22'] = sub1111
    st['dxy22'] = dxy1111
    st['dx22'] = dx1111
    st['dy22'] = dy1111
    df1 = pd.DataFrame(st)
    # print(influence_length, influence_breadth)
    # print(df1)
    return influence_length, influence_breadth


def points(length, breadth, grid_row, grid_column):
    point = []
    for r in np.linspace(0, length, grid_column):
        for s in np.linspace(0, breadth, grid_row):
            point.append((r, s))
    return point


def influence_point(point, influence):
    pts = {}
    x11 = []
    y11 = []
    k1 = []
    r1 = []
    x111 = []
    y111 = []
    for x1, y1 in point:
        inf = []
        k = 1
        for r in np.linspace(influence / 10, influence, 10):
            for theta in np.linspace(0, 360, 36):
                c = x1 + r * math.cos(theta)
                d = y1 + r * math.sin(theta)
                x11.append(x1)
                y11.append(y1)
                k1.append(k)
                r1.append(r)
                x111.append(c)
                y111.append(d)
            k += 1
    pts['x11'] = x11
    pts['y11'] = y11
    pts['k1'] = k1
    pts['r1'] = r1
    pts['x111'] = x111
    pts['y111'] = y111

    # print(len(inf))
    return pts


def Subsidence(influence_points, length, breadth, influence, thickness):
    S = [0.0323 / 36, 0.0911 / 36, 0.134 / 36, 0.1555 / 36, 0.1557 / 36, 0.1392 / 36, 0.1131 / 36, 0.0842 / 36,
         0.0579 / 36, 0.0369 / 36]
    inf = []
    for k, c, d in zip(influence_points['k1'], influence_points['x111'], influence_points['y111']):
        m = 0
        while m < len(Numbers_not_extracted):
            if list_x[m] <= c <= list_a[m]:
                inf.append(0)
            elif list_y[m] <= d <= list_b[m]:
                inf.append(0)
            else:
                inf.append(-thickness * S[k - 1])
    influence_points['sub'] = inf
    # print(S)
    return influence_points



def getter(entry_1, entry_2, entry_3, entry_4):
    global x, y, Gallery_width, Pillar_width, no_of__row, no_of__column
    Gallery_width = float(entry_1.get())
    Pillar_width = float(entry_2.get())
    no_of__row = float(entry_3.get())
    no_of__column = float(entry_4.get())
    x = (no_of__column * Pillar_width) + ((no_of__column + 1) * Gallery_width)
    y = (no_of__row * Pillar_width) + ((no_of__row + 1) * Gallery_width)


def gaiter(entry_1, entry_2, entry_3, entry_5, entry_6, entry_7):
    listx = []
    listy = []
    lista = []
    listb = []
    Depth = float(entry_1.get())
    Seam_thickness = float(entry_2.get())
    Numbers_not_extracted = list([int(x) for x in entry_3.get().split(",")])
    Angle = float(entry_5.get())
    grid_row = float(entry_6.get())
    grid_column = float(entry_7.get())

    t = 0
    while t < len(Numbers_not_extracted):
        listx.append(Gallery_width+(Gallery_width+Pillar_width)*(Numbers_not_extracted[t]%no_of__column))
        lista.append(Gallery_width+Pillar_width + (Gallery_width + Pillar_width) * (Numbers_not_extracted[t] % no_of__column))
        listy.append(Gallery_width + (Gallery_width + Pillar_width) * int((Numbers_not_extracted[t] / no_of__column)))
        listb.append(Gallery_width+Pillar_width + (Gallery_width + Pillar_width) * int((Numbers_not_extracted[t] / no_of__column)))
        print(Numbers_not_extracted[t])
        t=t+1
    print("Initial x coordinate",listx)
    print("Initial y coordinate",listy)
    print("Final x coordinate",lista)
    print("Final y coordinate",listb)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='GUI for Bord and Pillar', font=FONT)
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text='Bord and Pillar', command=lambda: controller.show_frame(PageOne))
        button1.pack(padx=10, pady=10)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Bord and Pillar', font=FONT)
        label.grid(padx=10, pady=10, row=0, column=0)
        label_1 = tk.Label(self, text='Gallery_width')
        label_2 = tk.Label(self, text="Pillar_width")
        label_3 = tk.Label(self, text="no_of_row")
        label_4 = tk.Label(self, text="no_of_column")

        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self)
        entry_3 = tk.Entry(self)
        entry_4 = tk.Entry(self)

        label_1.grid(row=1, column=1)
        entry_1.grid(row=2, column=1)
        label_2.grid(row=1, column=2)
        entry_2.grid(row=2, column=2)
        label_3.grid(row=3, column=1)
        entry_3.grid(row=4, column=1)
        label_4.grid(row=3, column=2)
        entry_4.grid(row=4, column=2)
        button7 = ttk.Button(self, text='Submit',
                             command=lambda: getter(entry_1, entry_2, entry_3, entry_4))
        button7.grid(row=9, column=1, columnspan=2, padx=10)

        button3 = ttk.Button(self, text='Show the Panel', command=lambda: PageOne.draw_graph(self))
        button3.grid(row=10, column=1, columnspan=2)
        button4 = ttk.Button(self, text='Calculate subsidence', command=lambda: controller.frome(PageTwo))
        button4.grid(row=11, column=1, columnspan=2)

        button1 = ttk.Button(self, text='Back to Main window', command=lambda: controller.show_frame(StartPage))
        button1.grid(row=12, column=1, columnspan=2)


    def draw_graph(self):
            global x, y, Gallery_width, Pillar_width, no_of__row, no_of__column
            root = Tk()
            self.frame = Frame(root, width=x, height=y)
            self.frame.grid(row=0, column=0)
            self.canvas = Canvas(self.frame, bg='green', width=x, height=y, scrollregion=(0, 0, (2 * x), (2 * y)))
            hbar = Scrollbar(self.frame, orient=HORIZONTAL)
            hbar.pack(side=BOTTOM, fill=X)
            hbar.config(command=self.canvas.xview)
            vbar = Scrollbar(self.frame, orient=VERTICAL)
            vbar.pack(side=RIGHT, fill=Y)
            vbar.config(command=self.canvas.yview)
            self.canvas.config(width=x, height=y)
            self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
            self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
            for i in range(int(no_of__row)):
                for j in range(int(no_of__column)):
                    a = (j + 1) * Gallery_width + j * Pillar_width
                    b = (i + 1) * Gallery_width + i * Pillar_width

                    self.canvas.create_rectangle(a, b, a + Pillar_width, b + Pillar_width, fill="blue", outline="red")
                    text_pos = (a + Pillar_width / 2, b + Pillar_width / 2)
                    text_content = "(%d)" % (j+(i*no_of__column))
                    self.canvas.create_text(text_pos, text=text_content)

            root.mainloop()

class PageTwo(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text='Bord and Pillar', font=FONT)
                label.grid(padx=10, pady=10, row=0, column=0)
                label_1 = tk.Label(self, text='Depth')
                label_2 = tk.Label(self, text="Seam Thickness")
                label_3 = tk.Label(self, text="Numbers associated with non extracted Pillars ")
                label_5 = tk.Label(self, text="Angle of Draw")
                label_6 = tk.Label(self, text='grid_row ')
                label_7 = tk.Label(self, text='grid_column ')
                entry_1 = tk.Entry(self)
                entry_2 = tk.Entry(self)
                entry_3 = tk.Entry(self)
                entry_5 = tk.Entry(self)
                entry_6 = tk.Entry(self)
                entry_7 = tk.Entry(self)
                button7 = ttk.Button(self, text='Submit',
                                     command=lambda: gaiter(entry_1, entry_2, entry_3, entry_5, entry_6, entry_7
                                                            ))

                label_1.grid(row=1, column=1)
                entry_1.grid(row=2, column=1)
                label_6.grid(row=1, column=2)
                entry_6.grid(row=2, column=2)
                label_7.grid(row=3, column=2)
                entry_7.grid(row=4, column=2)
                label_2.grid(row=3, column=1)
                entry_2.grid(row=4, column=1)

                label_3.grid(row=5, column=1)
                entry_3.grid(row=6, column=1)

                label_5.grid(row=9, column=1)
                entry_5.grid(row=10, column=1)
                button7.grid(row=10, column=3, columnspan=2, padx=10)

                button3 = ttk.Button(self, text='Show the Graph', command=lambda: controller.frome(PageThree))

                button3.grid(row=11, column=3, columnspan=2)

                button1 = ttk.Button(self, text='Back to Main window', command=lambda: controller.show_frame(StartPage))
                button1.grid(row=12, column=3, columnspan=2)
                self.output = tk.Text(self, font=FONT)
                self.output.grid(row=15, column=3)
                sys.stdout = self
                self.grid(row=16, column=3)

            def write(self, txt):
                self.output.insert(END, str(txt))





class PageThree(tk.Frame):
                    def __init__(self, parent, controller):
                        tk.Frame.__init__(self, parent)

                        label = ttk.Label(self, text='Graph for subsidence profile', font=FONT)
                        label.pack(padx=10, pady=10)
                        button1 = ttk.Button(self, text='Back to Main window',
                                             command=lambda: controller.show_frame(StartPage))
                        button1.pack()
                        button2 = ttk.Button(self, text='Draw Subsidence Graph',
                                             command=lambda: PageThree.draw_graph1(self))
                        button2.pack()
                        button3 = ttk.Button(self, text='Draw Displacement(x,y) Graph',
                                             command=lambda: PageThree.draw_graph_dxy(self))
                        button3.pack()
                        button4 = ttk.Button(self, text='Draw Displacement(x) Graph',
                                             command=lambda: PageThree.draw_graph_dx(self))
                        button4.pack()
                        button5 = ttk.Button(self, text='Draw Displacement(y)Graph',
                                             command=lambda: PageThree.draw_graph_dy(self))
                        button5.pack()
                        button6 = ttk.Button(self, text='Draw Strain(x) Graph',
                                             command=lambda: PageThree.draw_graph_sx(self))
                        button6.pack()
                    def draw_graph1(self):
                       global subsidence
                       global x1111, y1111, sub1111, dxy1111, dx1111, dy1111, str1111
                       c = np.unique(x1111)
                       d = np.unique(y1111)
                       C, D = np.meshgrid(c, d)
                       Z = np.array(sub1111).reshape(len(d), len(c))
                       f = Figure(figsize=(9, 9), dpi=100)
                       q = f.gca(projection='3d')
                       q.set_title("Subsidence Profile")
                       q.set_xlabel("Length")
                       q.set_ylabel("Breadth")
                       q.set_zlabel("Subsidence")
                       q.set_xlim([0, 3000])
                       q.set_ylim([0, 3000])

        # a.set_aspect('equal')

        # a.scatter(subsidence['x11'],subsidence['y11'])
                       q.plot_surface(C, D, Z, rstride=1, cstride=1, cmap=cm.jet)
                       canvas = FigureCanvasTkAgg(f, self)
                       canvas.show()
                       canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                       toolbar = NavigationToolbar2TkAgg(canvas, self)
                       toolbar.update()
                       canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    def draw_graph_dxy(self):
                        global subsidence
                        global x1111, y1111, sub1111, dxy1111, dx1111, dy1111, str1111
                        c = np.unique(x1111)
                        d = np.unique(y1111)
                        C, D = np.meshgrid(c, d)
                        Z = np.array(dxy1111).reshape(len(d), len(c))
                        f = Figure(figsize=(9, 9), dpi=100)
                        q = f.gca(projection='3d')
                        q.set_title("Displacement(x,y)")
                        q.set_xlabel("Length")
                        q.set_ylabel("Breadth")
                        q.set_zlabel("dxy")
                        # a.set_aspect('equal')

                        # a.scatter(subsidence['x11'],subsidence['y11'])
                        q.plot_surface(C, D, Z, cmap=cm.jet, cstride=1, rstride=1)
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.show()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2TkAgg(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    def draw_graph_dx(self):
                        global subsidence
                        global x1111, y1111, sub1111, dxy1111, dx1111, dy1111, str1111
                        c = np.unique(x1111)
                        d = np.unique(y1111)
                        C, D = np.meshgrid(c, d)
                        Z = np.array(dx1111).reshape(len(d), len(c))
                        f = Figure(figsize=(9, 9), dpi=100)
                        q = f.gca(projection='3d')
                        q.set_title("Dislacement(x) profile")
                        q.set_xlabel("Length")
                        q.set_ylabel("Breadth")
                        q.set_zlabel("dx")
                        # a.set_aspect('equal')

                        # a.scatter(subsidence['x11'],subsidence['y11'])
                        q.plot_surface(C, D, Z, cmap=cm.jet, cstride=1, rstride=1)
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.show()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2TkAgg(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    def draw_graph_dy(self):
                        global subsidence
                        global x1111, y1111, sub1111, dxy1111, dx1111, dy1111, str1111
                        c = np.unique(x1111)
                        d = np.unique(y1111)
                        C, D = np.meshgrid(c, d)
                        Z = np.array(dy1111).reshape(len(d), len(c))
                        f = Figure(figsize=(9, 9), dpi=100)
                        q = f.gca(projection='3d')
                        q.set_title("displacement(y) profile")
                        q.set_xlabel("Length")
                        q.set_ylabel("Breadth")
                        q.set_zlabel("dy")
                        # a.set_aspect('equal')

                        # a.scatter(subsidence['x11'],subsidence['y11'])
                        q.plot_surface(C, D, Z, rstride=1, cstride=1, cmap=cm.jet)
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.show()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2TkAgg(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                    def draw_graph_sx(self):
                        global subsidence
                        global x1111, y1111, sub1111, dxy1111, dx1111, dy1111, str1111
                        c = np.unique(x1111)
                        d = np.unique(y1111)
                        C, D = np.meshgrid(c, d)
                        Z = np.array(sub1111).reshape(len(d), len(c))
                        f = Figure(figsize=(9, 9), dpi=100)
                        q = f.gca(projection='3d')
                        q.set_title("Subsidence Profile")
                        q.set_xlabel("Length")
                        q.set_ylabel("Breadth")
                        q.set_zlabel("Subsidence")
                        # a.set_aspect('equal')

                        # a.scatter(subsidence['x11'],subsidence['y11'])
                        q.plot_surface(C, D, Z, rstride=1, cstride=1, cmap=cm.jet)
                        canvas = FigureCanvasTkAgg(f, self)
                        canvas.show()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                        toolbar = NavigationToolbar2TkAgg(canvas, self)
                        toolbar.update()
                        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    app = GUI()
    app.mainloop()