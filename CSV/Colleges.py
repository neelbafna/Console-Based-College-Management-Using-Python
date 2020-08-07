import csv
import sys
import os.path
#if file exist no action taken and if not column headers are added to the CSV file.
if not os.path.isfile("college.csv"):
	row_list = [["College ID", "College Name", "Course Type" , "City" , "Fees" , "PinCode"]]
	with open('college.csv','w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerows(row_list)

class College(object):
	def __init__(self, collegeId, collegeName, courseType, city, fees, pinCode):
		self.collegeId=collegeId
		self.collegeName=collegeName
		self.courseType=courseType
		self.city=city
		self.fees=fees
		self.pinCode=pinCode

def start():
	print("1. Register College \n2. Find\n3. Delete\n4. Exit")
	inp = input()
	keep_running=True
	while keep_running:

		#Register new college
		if inp == "1":
			flag=True
			#Check is ID is already present
			print("\n\ncollege ID")
			identity= input()
			with open('college.csv', 'r',) as file:
				reader = csv.reader(file, delimiter = ',')
				for row in reader:
					if identity == row[0]:
						print(row)
						flag=False
			if flag:
				print("\nCollege Name")
				name=input()
				print("\nCourse Type")
				course=input()
				print("\nCity")
				city=input()
				print("\nFees")
				fees=input()
				print("\nPin Code")
				code=input()
				print("\n\nCollege Registered Successfully")
				print("\n\n1. Register College \n2. Find\n3. Delete\n4. Exit")
				inp=input()
				c1=College(identity,name,course,city,fees,code)
				row_list = [[c1.collegeId,c1.collegeName,c1.courseType,c1.city,c1.fees,c1.pinCode]]
				with open('college.csv', 'a', newline='') as file:
					writer = csv.writer(file)
					writer.writerows(row_list)

		#Find College Details
		if inp == '2':
			isPresent=False
			print("\n\nEnter City")
			find_city=input()
			print("\nEnter Course")
			find_course=input()
			with open('college.csv', 'r',) as file:
				reader = csv.reader(file, delimiter = ',')
				for row in reader:
					#input case wont matter as comaring ckecks by converting to lowercase
					if find_city.lower() == row[3].lower() and find_course.lower() ==row[2].lower():
						print("\n\nName : ",row[1])
						print("College ID : ",row[0])
						print("Fees : ",row[4])
						print("Pincode : ",row[5])
						isPresent=True
			if not isPresent:
				print("\n\nNo Colleges Found")
			print("\n\n1. Register College \n2. Find\n3. Delete\n4. Exit")
			inp=input()


		#Delete college with matching ID
		if inp == '3':
			lines=list()
			isThere = False
			print("\n\nEnter College ID to br Deleted")
			identity = input()
			with open('college.csv', 'r',) as file:
				reader = csv.reader(file, delimiter = ',')
				for row in reader:
					#list of list is created where each sublist contains every single row of csv file
				    lines.append(row)
				    for field in row:
				        if field == identity:
				        	#if matching ID found in row the row(i.e. Sublist) is removed 
				            lines.remove(row)
				            isThere = True
				    #res = list(filter(None, lines))
				#new list is written to file 
				with open('college.csv', 'w',newline="") as writeFile:
				    writer = csv.writer(writeFile)
				    writer.writerows(lines)
			#if ID not found displays appropriate message
			if not isThere:
				print("\n\nCollege Not Found")
			else:
					print("\n\nDeleted Successfully")
			print("\n\n1. Register College \n2. Find\n3. Delete\n4. Exit")
			inp=input()

		#exit
		if inp == '4':
			print("\n\nThank You")
			keep_running=False
start()