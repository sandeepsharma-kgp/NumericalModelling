import tkinter as tk
from tkinter import ttk
from tkinter import *
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import math
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors, ticker, cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
style.use('ggplot')

FONT=('verdana',12)
subsidence={}
sub1111=[]
x1111=[]
y1111=[]
dxy1111=[]
dx1111=[]
dy1111=[]
str1111=[]
subsidence_x={}
xsub1111=[]
xx1111=[]
xy1111=[]
xdxy1111=[]
xdx1111=[]
xdy1111=[]
xstr1111=[]
subsidence_y={}
ysub1111=[]
yx1111=[]
yy1111=[]
ydxy1111=[]
ydx1111=[]
ydy1111=[]
ystr1111=[]
class GUI(tk.Tk):
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		container=tk.Frame(self)

		container.pack(side='top',fill='both',expand=True)

		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.frames={}

		for F in (StartPage,PageOne,PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven):

			frame=F(container,self)

			self.frames[F]=frame

			frame.grid(row=0,column=0,sticky='nsew')

		self.show_frame(StartPage)

	def show_frame(self,cont):

		frame=self.frames[cont]
		frame.tkraise()
	def frome(self,cont):
		frame=self.frames[cont]
		frame.tkraise()
def Influence_area(depth,length,breadth,draw,thickness,no_of_grids_row,no_of_grids_column,xv,yv):
	global subsidence
	global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
	global subsidence_x
	global xx1111,xy1111,xsub1111,xdxy1111,xdx1111,xdy1111,xstr1111
	global subsidence_y
	global yx1111,yy1111,ysub1111,ydxy1111,ydx1111,ydy1111,ystr1111
	
	Influence=depth*math.tan(math.radians(draw))
	influence_length=length+2*Influence
	influence_Breadth=breadth+2*Influence
	point=points(influence_length,influence_Breadth,no_of_grids_row,no_of_grids_column)
	point_x = points_x(xv,influence_Breadth,no_of_grids_row,no_of_grids_column)
	point_y = points_y(influence_length,yv,no_of_grids_row,no_of_grids_column)


	influence_points=influence_point(point,Influence)
	influence_points_x = influence_point(point_x,Influence)
	influence_points_y = influence_point(point_y,Influence)
	subsidence=Subsidence(influence_points,length,breadth,Influence,thickness)
	subsidence_x=Subsidence(influence_points_x,length,breadth,Influence,thickness)
	subsidence_y=Subsidence(influence_points_y,length,breadth,Influence,thickness)
	dxy1=[]
	dx1=[]
	dy1=[]
	xdxy1=[]
	xdx1=[]
	xdy1=[]
	ydxy1=[]
	ydx1=[]
	ydy1=[]

	'''for x11,y11,x111,y111,sub in zip(subsidence['x11'],subsidence['y11'],subsidence['x111'],subsidence['y111'],subsidence['sub']):
		dist=math.sqrt((x111-x11)**2+(y111-y11)**2)
		tanAlpha=dist/depth
		dxy1.append(sub*tanAlpha)'''

	for x11,y11,x111,y111,sub in zip(subsidence['x11'],subsidence['y11'],subsidence['x111'],subsidence['y111'],subsidence['sub']):
		tanAlpha=math.sqrt(((x111-(Influence+0.5*breadth))**2+(y111-(Influence+0.5*length))**2))/depth
		dxy1.append(sub*tanAlpha)
		Beta=math.acos((x111-(Influence+0.5*breadth))/(math.sqrt((x111-(Influence+0.5*breadth))**2+(y111-(Influence+0.5*length))**2)))
		Beta1=math.acos((y111-(Influence+0.5*length))/(math.sqrt((x111-(Influence+0.5*breadth))**2+(y111-(Influence+0.5*length))**2)))
		dx1.append(sub*tanAlpha*math.cos(Beta))
		dy1.append(sub*tanAlpha*math.cos(Beta1))
	for xx11,xy11,xx111,xy111,xsub in zip(subsidence_x['x11'],subsidence_x['y11'],subsidence_x['x111'],subsidence_x['y111'],subsidence_x['sub']):
		tanAlpha=math.sqrt(((xx111-(Influence+0.5*breadth))**2+(xy111-(Influence+0.5*length))**2))/depth
		xdxy1.append(xsub*tanAlpha)
		Beta=math.acos((xx111-(Influence+0.5*breadth))/(math.sqrt((xx111-(Influence+0.5*breadth))**2+(xy111-(Influence+0.5*length))**2)))
		Beta1=math.acos((xy111-(Influence+0.5*length))/(math.sqrt((xx111-(Influence+0.5*breadth))**2+(xy111-(Influence+0.5*length))**2)))
		xdx1.append(xsub*tanAlpha*math.cos(Beta))
		xdy1.append(xsub*tanAlpha*math.cos(Beta1))
	for yx11,yy11,yx111,yy111,ysub in zip(subsidence_y['x11'],subsidence_y['y11'],subsidence_y['x111'],subsidence_y['y111'],subsidence_y['sub']):
		tanAlpha=math.sqrt(((yx111-(Influence+0.5*breadth))**2+(yy111-(Influence+0.5*length))**2))/depth
		ydxy1.append(sub*tanAlpha)
		Beta=math.acos((yx111-(Influence+0.5*breadth))/(math.sqrt((yx111-(Influence+0.5*breadth))**2+(yy111-(Influence+0.5*length))**2)))
		Beta1=math.acos((yy111-(Influence+0.5*length))/(math.sqrt((yx111-(Influence+0.5*breadth))**2+(yy111-(Influence+0.5*length))**2)))
		ydx1.append(ysub*tanAlpha*math.cos(Beta))
		ydy1.append(ysub*tanAlpha*math.cos(Beta1))


	subsidence['dxy']=dxy1
	subsidence['dx']=dx1
	subsidence['dy']=dy1

	subsidence_x['dxy']=xdxy1
	subsidence_x['dx']=xdx1
	subsidence_x['dy']=xdy1

	subsidence_y['dxy']=ydxy1
	subsidence_y['dx']=ydx1
	subsidence_y['dy']=ydy1

	df=pd.DataFrame(subsidence)
	df2=pd.DataFrame(subsidence_x)
	df3=pd.DataFrame(subsidence_y)


	for x,y in point:
		z=df['sub'][(df['x11']==x) & (df['y11']==y)]
		dxy=df['dxy'][(df['x11']==x) & (df['y11']==y)]
		dx=df['dx'][(df['x11']==x) & (df['y11']==y)]
		dy=df['dy'][(df['x11']==x) & (df['y11']==y)]
		sub1111.append(z.sum())
		x1111.append(x)
		y1111.append(y)
		dxy1111.append(dxy.sum())
		dx1111.append(dx.sum())
		dy1111.append(dy.sum())
	for x,y in point_x:
		xz=df2['sub'][(df2['x11']==x) & (df2['y11']==y)]
		xdxy=df2['dxy'][(df2['x11']==x) & (df2['y11']==y)]
		xdx=df2['dx'][(df2['x11']==x) & (df2['y11']==y)]
		xdy=df2['dy'][(df2['x11']==x) & (df2['y11']==y)]
		xsub1111.append(xz.sum())
		xx1111.append(x)
		xy1111.append(y)
		xdxy1111.append(xdxy.sum())
		xdx1111.append(xdx.sum())
		xdy1111.append(xdy.sum())
	for x,y in point_y:
		yz=df3['sub'][(df3['x11']==x) & (df3['y11']==y)]
		ydxy=df3['dxy'][(df3['x11']==x) & (df3['y11']==y)]
		ydx=df3['dx'][(df3['x11']==x) & (df3['y11']==y)]
		ydy=df3['dy'][(df3['x11']==x) & (df3['y11']==y)]
		ysub1111.append(yz.sum())
		yx1111.append(x)
		yy1111.append(y)
		ydxy1111.append(ydxy.sum())
		ydx1111.append(ydx.sum())
		ydy1111.append(ydy.sum())
	st={}
	st['x22']=x1111
	st['y22']=y1111
	st['s22']=sub1111
	st['dxy22']=dxy1111
	st['dx22']=dx1111
	st['dy22']=dy1111
	fw = open('subsidence.csv','w')
	for p,q,r,s,t,u in zip(st['x22'],st['y22'],st['s22'],st['dxy22'],st['dx22'],st['dy22']):
		fw.write(str(p)+','+str(q)+','+str(r)+','+str(s)+','+str(t)+','+str(u)+'\n')
	fw.close()
	df1=pd.DataFrame(st)
	print (influence_length,influence_Breadth)
	print("fuck off")
	return influence_length,influence_Breadth
def points(length,breadth,grids=20,cols=30):	
	point=[]
	for i in np.linspace(0,length,cols):
		for j in np.linspace(0,breadth,grids):
			point.append((i,j))
	return point
def points_x(length,breadth,grids=20,cols=30):
	point_x=[]
	for i in np.linspace(0,breadth,grids):
		point_x.append((length,i))
	return point_x
def points_y(length,breadth,grids=20,cols=30):
	point_y=[]
	for i in np.linspace(0,length,cols):
		point_y.append((i,breadth))
	return point_y
def influence_point(point,Influence):
	pts={}
	x11=[]
	y11=[]
	k1=[]
	r1=[]
	x111=[]
	y111=[]
	for x1,y1 in point:
		k=1
		for r in np.linspace(Influence/10,Influence,10):
			for theta in np.linspace(0,360,36):
				x=x1+r*math.cos(theta)
				y=y1+r*math.sin(theta)
				x11.append(x1)
				y11.append(y1)
				k1.append(k)
				r1.append(r)
				x111.append(x)
				y111.append(y)
			k+=1
	pts['x11']=x11
	pts['y11']=y11
	pts['k1']=k1
	pts['r1']=r1
	pts['x111']=x111
	pts['y111']=y111

	return pts


def Subsidence(influence_points,length,breadth,Influence,thickness):
    S=[0.0323/36,0.0911/36,0.134/36,0.1555/36,0.1557/36,0.1392/36,0.1131/36,0.0842/36,0.0579/36,0.0369/36]
    inf=[]
    for k,x,y in zip(influence_points['k1'],influence_points['x111'],influence_points['y111']):
        if y>Influence+breadth:
            inf.append(0)
        elif x<Influence :
            inf.append(0)
        elif x>Influence+length:
        	inf.append(0)
        elif y<Influence:
        	inf.append(0)
        else :
            inf.append(-thickness*S[k-1])
    influence_points['sub']=inf
    print(S)
    return influence_points
        
        
        
        
def getter(entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9):
	
	Depth=float(entry_1.get())
	Seam_thickness=float(entry_2.get())
	Length = float(entry_3.get())
	Breadth = float(entry_4.get())
	Angle = float(entry_5.get())
	Number_of_grids_row= float(entry_6.get())
	Number_of_grids_column= float(entry_7.get())
	xv = float(entry_8.get())
	yv = float(entry_9.get())
	influence_length,influence_breath=Influence_area(Depth,Length,Breadth,Angle,Seam_thickness,Number_of_grids_row,Number_of_grids_column,xv,yv)




class StartPage(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label=tk.Label(self,text='GUI for Subsidence',font=FONT)
		label.pack(padx=10,pady=10)

		button1=ttk.Button(self,text='Longwall',command=lambda:controller.show_frame(PageOne))
		button1.pack(padx=10,pady=10)

class PageOne(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)

		label=tk.Label(self,text='Long Wall',font=FONT)
		label.grid(padx=10,pady=10,row=0,column=0)
		label_1=tk.Label(self,text='Depth')
		label_2=tk.Label(self,text="Seam Thickness")
		label_3=tk.Label(self,text="Length")
		label_4=tk.Label(self,text="Breadth")
		label_5=tk.Label(self,text="Angle of Draw")
		label_6=tk.Label(self,text='Number of grids per row : ')
		label_7=tk.Label(self,text="Number of grids per column : ")
		label_8 = tk.Label(self,text="x")
		label_9 = tk.Label(self,text="y")



		entry_1=tk.Entry(self)
		entry_2=tk.Entry(self)
		entry_3=tk.Entry(self)
		entry_4=tk.Entry(self)
		entry_5=tk.Entry(self)
		entry_6=tk.Entry(self)
		entry_7=tk.Entry(self)
		entry_8=tk.Entry(self)
		entry_9=tk.Entry(self)


		button7=ttk.Button(self,text='Submit',command=lambda:getter(entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9))

		label_1.grid(row=1,column=1)
		entry_1.grid(row=2,column=1)
		label_6.grid(row=1,column=2)
		entry_6.grid(row=1,column=3)

		label_2.grid(row=3,column=1)
		entry_2.grid(row=4,column=1)
		label_7.grid(row=3,column=2)
		entry_7.grid(row=3,column=3)

		label_3.grid(row=5,column=1)
		entry_3.grid(row=6,column=1)

		label_4.grid(row=7,column=1)
		entry_4.grid(row=8,column=1)

		label_5.grid(row=9,column=1)
		entry_5.grid(row=10,column=1)

		label_8.grid(row = 11,column=1)
		entry_8.grid(row = 12,column=1)

		label_9.grid(row = 13,column=1)
		entry_9.grid(row = 14,column=1)

		button7.grid(row=15,column=3,columnspan=2,padx=10)

		button3=ttk.Button(self,text='Show the Graph',command=lambda :controller.frome(PageTwo))

		button3.grid(row=16,column=1,columnspan=2)

		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.grid(row=17,column=1,columnspan=2)
	def write(self, txt):
		self.output.insert(END,str(txt))
		
class PageTwo(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for subsidence profile',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:PageTwo.draw_graph(self))
		button2.pack()
		button3=ttk.Button(self,text='Displacement(x,y) Graph',command=lambda:controller.show_frame(PageThree))
		button3.pack()
		button4=ttk.Button(self,text='Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
		button7 = ttk.Button(self,text='subsidence(x) profile',command=lambda:controller.show_frame(PageSeven))
		button7.pack()
	def draw_graph(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(sub1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Subsidence Profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_xlim([0,3000])
		#a.set_ylim([0,3000])

		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contourf(X,Y,Z)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

	
class PageThree(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for d(x,y) profile',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Draw Displacement(x,y) Graph',command=lambda:PageThree.draw_graph_dxy(self))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()

	def draw_graph_dxy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dxy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x,y)")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contourf(X,Y,Z,cmap=cm.jet)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
	
class PageFour(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for displacement(x)',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Displacement(x,y) Graph',command=lambda:controller.show_frame(PageThree))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:PageFour.draw_graph_dx(self))
		button4.pack()
		button5=ttk.Button(self,text='Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
	
	def draw_graph_dx(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dx1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x) profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contourf(X,Y,Z)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
	
class PageFive(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for displacement(y)',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Displacement(x,y) Graph',command=lambda:controller.show_frame(PageThree))
		button3.pack()
		button4=ttk.Button(self,text='Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:PageFive.draw_graph_dy(self))
		button5.pack()
		button6=ttk.Button(self,text='Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
	
	def draw_graph_dy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("displacement(y) profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contourf(X,Y,Z)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
	
class PageSix(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for strain',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Displacement(x,y) Graph',command=lambda:controller.show_frame(PageThree))
		button3.pack()
		button4=ttk.Button(self,text='Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:PageSix.draw_graph_sx(self))
		button6.pack()
	def draw_graph_sx(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(sub1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("strain profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
	
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur = a.contourf(X,Y,Z,rstride=1,cstride=1,cmap=cm.jet)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
class PageSeven(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Subsidence along breadth',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Draw Displacement(x,y) Graph',command=lambda:PageThree.draw_graph_dxy(self))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
		button7=ttk.Button(self,text='Draw subsidence(x) along breadth Graph',command=lambda:PageSeven.draw_graph_dxy(self))
		button7.pack()


	def draw_graph_dxy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		global subsidence_x
		global xx1111,xy1111,xsub1111,xdxy1111,xdx1111,xdy1111,xstr1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dxy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Subsidence along breadth")
		a.set_xlabel("Breadth")
		a.set_ylabel("Subsidence")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		a.plot(xy1111,xsub1111)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
class PageEight(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for d(x,y) profile',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Draw Displacement(x,y) Graph',command=lambda:PageThree.draw_graph_dxy(self))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
		button7=ttk.Button(self,text='Draw subsidence(x) Graph',command=lambda:PageSeven.draw_graph_dxy(self))
		button7.pack()


	def draw_graph_dxy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		global subsidence_x
		global xx1111,xy1111,xsub1111,xdxy1111,xdx1111,xdy1111,xstr1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dxy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x,y)")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		a.scatter(xy1111,xsub1111)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

class PageNine(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for d(x,y) profile',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Draw Displacement(x,y) Graph',command=lambda:PageThree.draw_graph_dxy(self))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
		button7=ttk.Button(self,text='Draw subsidence(x) Graph',command=lambda:PageSeven.draw_graph_dxy(self))
		button7.pack()


	def draw_graph_dxy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		global subsidence_x
		global xx1111,xy1111,xsub1111,xdxy1111,xdx1111,xdy1111,xstr1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dxy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x,y)")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		a.scatter(xy1111,xsub1111)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
class PageTen(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for d(x,y) profile',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Draw Displacement(x,y) Graph',command=lambda:PageThree.draw_graph_dxy(self))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
		button7=ttk.Button(self,text='Draw subsidence(x) Graph',command=lambda:PageSeven.draw_graph_dxy(self))
		button7.pack()


	def draw_graph_dxy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		global subsidence_x
		global xx1111,xy1111,xsub1111,xdxy1111,xdx1111,xdy1111,xstr1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dxy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x,y)")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		a.scatter(xy1111,xsub1111)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

class PageEleven(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for d(x,y) profile',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:controller.show_frame(PageTwo))
		button2.pack()
		button3=ttk.Button(self,text='Draw Displacement(x,y) Graph',command=lambda:PageThree.draw_graph_dxy(self))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:controller.show_frame(PageFour))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:controller.show_frame(PageFive))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:controller.show_frame(PageSix))
		button6.pack()
		button7=ttk.Button(self,text='Draw subsidence(x) Graph',command=lambda:PageSeven.draw_graph_dxy(self))
		button7.pack()


	def draw_graph_dxy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		global subsidence_x
		global xx1111,xy1111,xsub1111,xdxy1111,xdx1111,xdy1111,xstr1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dxy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x,y)")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		a.scatter(xy1111,xsub1111)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
class Pageinf(tk.Frame):

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		label=ttk.Label(self,text='Graph for subsidence profile',font=FONT)
		label.pack(padx=10,pady=10)
		button1=ttk.Button(self,text='Back to Main window',command=lambda:controller.show_frame(StartPage))
		button1.pack()
		button2=ttk.Button(self,text='Draw Subsidence Graph',command=lambda:PageTwo.draw_graph(self))
		button2.pack()
		button3=ttk.Button(self,text='Draw Displacement(x,y) Graph',command=lambda:PageTwo.draw_graph_dxy(self))
		button3.pack()
		button4=ttk.Button(self,text='Draw Displacement(x) Graph',command=lambda:PageTwo.draw_graph_dx(self))
		button4.pack()
		button5=ttk.Button(self,text='Draw Dispacement(y)Graph',command=lambda:PageTwo.draw_graph_dy(self))
		button5.pack()
		button6=ttk.Button(self,text='Draw Strain(x) Graph',command=lambda:PageTwo.draw_graph_sx(self))
		button6.pack()
	def draw_graph(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(sub1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Subsidence Profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_xlim([0,3000])
		#a.set_ylim([0,3000])

		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contour(X,Y,Z)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

	def draw_graph_dxy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dxy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x,y)")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contour(X,Y,Z,cmap=cm.jet)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
	def draw_graph_dx(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dx1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Displacement(x) profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contour(X,Y,Z)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
	def draw_graph_dy(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(dy1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("displacement(y) profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur=a.contour(X,Y,Z)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
	def draw_graph_sx(self):
		global subsidence
		global x1111,y1111,sub1111,dxy1111,dx1111,dy1111,str1111
		x=np.unique(x1111)
		y=np.unique(y1111)
		X,Y = np.meshgrid(x,y)
		Z=np.array(sub1111).reshape(len(y),len(x))
		f=Figure(figsize=(9,9),dpi=100)
		a=f.gca()
		a.set_title("Subsidence Profile")
		a.set_xlabel("Length")
		a.set_ylabel("Breadth")
	
		#a.set_aspect('equal')

		#a.scatter(subsidence['x11'],subsidence['y11'])
		sur = a.contour(X,Y,Z,rstride=1,cstride=1,cmap=cm.jet)
		f.colorbar(sur)
		canvas=FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

		toolbar=NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

if __name__ == '__main__':
	app=GUI()
	app.mainloop()
