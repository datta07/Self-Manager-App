import time
import sqlite3

#options to add the birthdays




class Manager:

	#----------------------------------------------
	def __init__(self,date=time.strftime("%d/%m/%Y")):
		self.wisher()
		date=date.split('/')
		for no in range(3):
			date[no]=str(int(date[no]))
		date='/'.join(date)
		self.date=date
		self.calData=self.calenderDataFetch()
		self.day=self.calData[4]
		self.month=self.calData[2]
		self.teluguYear=self.calData[5]
		self.teluguMonth=self.calData[6]
		self.rutulu=self.calData[7]
		self.ayanam=self.calData[8]
		#---------------------------------
		self.importantDays=self.calData[9]
		self.virathaDays=self.calData[10]
		self.Festials=self.calData[11]
		#---------------------------------
		self.sunrise=self.calData[12]
		self.sunset=self.calData[13]
		self.thithi=self.calData[14]
		self.nakshitram=self.calData[15]
		#---------------------------------
		self.isHoliday=self.calData[17]
		self.holiday=self.calData[16]
		try:
			self.Facebook=self.calData[-1].split('$')
		except Exception:
			self.Facebook=[]

	def calenderDataFetch(self):
		con=sqlite3.connect('calender.db')
		mat=con.execute('SELECT * FROM main_table WHERE DATE=?',(self.date,))
		arr=[]
		for i in mat:
			for j in i:
				arr.append(j)
		return arr
	#----------------------------------------------
	#all the numbers are replaced by T+str(no)
	#change in protocode is required
	#07-11-2019






	#----------------------------------------------	
	def wisher(self):
		self.lineDrawer()
		hr=int(time.strftime('%H'))
		if (hr>16):
			print('Good evening')
		elif (hr>12):
			print('Good afternoon')
		elif (hr>4):
			print('Good Morning')
		else:
			print('Its Too late')

	def lineDrawer(self,no=30,times=1,endl='\n'):
		for i in range(times):
			print('-'*no,end=endl)

	def DayDetails(self):
		self.lineDrawer()
		print(self.date,'\t',self.day)
		print(self.sunrise,'\t    ',self.sunset)
		self.lineDrawer()
		print(self.thithi,'\t  ',self.nakshitram)
		self.lineDrawer()
		print(self.teluguYear)
		print(self.teluguMonth,self.rutulu,self.ayanam)
		self.lineDrawer()
		daySpecial={self.importantDays,self.Festials}
		daySpecial.remove('-')
		if (self.virathaDays!='-'):
			print(self.virathaDays)
		if (len(daySpecial)>=1):
			print("todays Importance :-")
			for i in daySpecial:
				print(i)
			if (self.holiday!='-'):
				print('Holiday today because',self.holiday)
			elif (self.isHoliday==1):
				print('today is Holiday')
			self.lineDrawer()
		if (len(self.Facebook)>0):
			print('Todays birthdays :-')
			for i in self.Facebook:
				print(i)
			self.lineDrawer()





man=Manager()
data=man.calenderDataFetch()
man.DayDetails()
'''for i,no in zip(data,range(len(data))):
	print(no,i)
print(man.importantDays)'''