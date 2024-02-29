import tkinter as tk
class MyButton(tk.Button):
	tugmalar = []
	
	def __init__(self, oyna,numer, x, y, *args, **kwargs):
		super(MyButton, self).__init__(oyna, width=12,height=6, bd=5, font=('arial', 15, 'bold'), *args, **kwargs)
		self.Tugmalar = {}
		self.x = x
		self.y = y
		self.numer = numer
		self.Tugmalar['numer'] = self.numer
		self.X_0 = 0
		self.Tugmalar['X_0'] = self.X_0
		self.mantiq = True
		self.tugmalar.append(self.Tugmalar)
class Tugmalar():
	s = 0
	Row = 3
	Column = 3
	win = tk.Tk()
	win.title('X va 0 o\'yini')
	a = tk.Label(win, text='Natija', height=2, bg='gray')
	a.grid(row=3, columnspan=2, stick='wens')
	def __init__(self):
		qadam = 0
		self.tugmalar = []
		
		for i in range(Tugmalar.Row):
			tugma = []
			for j in range(Tugmalar.Column):
				qadam += 1
				btn = MyButton(Tugmalar.win, x=i, y=j, numer=qadam)
				tugma.append(btn)
				btn.config(command=lambda button=btn: self.Bosish(button))
			self.tugmalar.append(tugma)
	def Btn(self):
		for i in range(Tugmalar.Row):
			for j in range(Tugmalar.Column):
				btn = self.tugmalar[i][j]
				btn.grid(row=i, column=j)
	def Bosish(self, btn_bosish: MyButton):
		btnlar = MyButton.tugmalar
		Tugmalar.s += 1
		if Tugmalar.s % 2 == 0:
			if btn_bosish.mantiq:
				btn_bosish.mantiq = False
				btn_bosish.config(text="x", bg='red')
				btn_bosish.Tugmalar['X_0'] = 4
				if (btnlar[0]['X_0'] + btnlar[1]['X_0'] + btnlar[2]['X_0']) == 12:
					MyButton.mantiq = False
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
				elif (btnlar[0]['X_0'] + btnlar[4]['X_0'] + btnlar[8]['X_0']) == 12:
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
				elif (btnlar[0]['X_0'] + btnlar[3]['X_0'] + btnlar[6]['X_0']) == 12:
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
				elif (btnlar[3]['X_0'] + btnlar[4]['X_0'] + btnlar[5]['X_0']) == 12:
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
				elif (btnlar[2]['X_0'] + btnlar[4]['X_0'] + btnlar[6]['X_0']) == 12:
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
				elif (btnlar[2]['X_0'] + btnlar[5]['X_0'] + btnlar[8]['X_0']) == 12:
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
				elif (btnlar[6]['X_0'] + btnlar[7]['X_0'] + btnlar[8]['X_0']) == 12:
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
				elif (btnlar[1]['X_0'] + btnlar[4]['X_0'] + btnlar[7]['X_0']) == 12:
					self.Tozala()
					return Tugmalar.a.config(text="X yutdi")
		else:
			if btn_bosish.mantiq:
				btn_bosish.mantiq = False
				btn_bosish.Tugmalar['X_0'] = 3
				btn_bosish.config(text="0", bg='gray')
				if (btnlar[0]['X_0'] + btnlar[1]['X_0'] + btnlar[2]['X_0']) == 9:
					self.Tozala()
					return Tugmalar.a.config(text="0 yutdi")
				elif (btnlar[0]['X_0'] + btnlar[4]['X_0'] + btnlar[8]['X_0']) == 9:
					self.Tozala()
					return Tugmalar.a.config(text="0 yutdi")
				elif (btnlar[0]['X_0'] + btnlar[3]['X_0'] + btnlar[6]['X_0']) == 9:
					self.Tozala()
					return Tugmalar.a.config(text="0 yutdi")
				elif (btnlar[3]['X_0'] + btnlar[4]['X_0'] + btnlar[5]['X_0']) == 9:
					self.Tozala()
					return Tugmalar.a.config(text="0 yutdi")
				elif (btnlar[2]['X_0'] + btnlar[4]['X_0'] + btnlar[6]['X_0']) == 9:
					self.Tozala()
					return Tugmalar.a.config(text="0 yutdi")
				elif (btnlar[2]['X_0'] + btnlar[5]['X_0'] + btnlar[8]['X_0']) == 9:
					self.Tozala()
					return Tugmalar.a.config(text="0 yutdi")
				elif (btnlar[6]['X_0'] + btnlar[7]['X_0'] + btnlar[8]['X_0']) == 9:
					MyButton.mantiq = False
					self.Tozala()
				elif (btnlar[1]['X_0'] + btnlar[4]['X_0'] + btnlar[7]['X_0']) == 9:
					self.Tozala()
					return Tugmalar.a.config(text="0 yutdi")
	def Tozala(self):
		for i in range(Tugmalar.Row):
			for j in range(Tugmalar.Column):
				btn = self.tugmalar[i][j]
				btn.mantiq = True
				Tugmalar.s = 0
				btn.config(text='', bg='white')
		for btn in MyButton.tugmalar:
			btn['X_0'] = 0

	def Start(self):
		tk.Button(Tugmalar.win, text='Restart',bd=5, height=2, bg='gray', command=lambda: self.Tozala()).grid(row=3,column=2,stick='wens')
		self.Btn()
		Tugmalar.win.mainloop()
x = Tugmalar()
x.Start()


print(MyButton.tugmalar)