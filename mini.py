import sys

def initial_phonebook():
	rows, cols = int(input("Please, enter number of contacts you want to store ? ")), 5
	phone_book = []
	print(phone_book)
	for i in range(rows):
		print("\nEnter contact details in the following order (ONLY):")
		print("NOTE: * indicates mandatory fields")
		print("....................................................................")
		temp = []
		for j in range(cols):			
			#name
			if j == 0:
				temp.append(str(input("Enter name*: ")))
				if temp[j] == '' or temp[j] == ' ':
					sys.exit("Name is a mandatory field.\n Process exiting due to blank field...")	
			#number
			if j == 1:
				temp.append(int(input("Enter contact number*: ")))
				if len(temp)!= 10:
					print("Contact no. should be 10 digits")	
			#e-mail address
			if j == 2:
				temp.append(str(input("Enter e-mail address: ")))
				if temp[j] !='':
					while "@" not in temp[j]:
						temp[j] = input("Your email address must have '@' in it\nPlease write your email address again : ")
						if "." not in temp[j]:
							temp[j] = input("Your email address must have '.' in it\nPlease write your email address again : ")
				if temp[j] == '' or temp[j] == ' ':
					temp[j] = None
			#DOB
			if j == 3:
				temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
				if temp[j] !='':
					from datetime import datetime
					test_str = temp[j]
					format = "%d/%m/%Y"
					res = True
					try:
						res = bool(datetime.strptime(test_str, format))
					except ValueError:
						res = False
					if res == False :
						temp[j]=input("Invalid date format\nPlease enter valid date format : ")
				if temp[j] == '' or temp[j] == ' ':
						temp[j] = None
			#category
			if j == 4:
				temp.append(str(input("Enter category(Family(F)/Friends(FR)/Work(W)/Others(O)): ")))
				if temp[j] == "" or temp[j] == ' ':
					temp[j] = None
		phone_book.append(temp)	
	print(phone_book)
	return phone_book
def menu():
	print("********************************************************************")
	print("\t\t\tPHONE DIRECTORY")
	print("********************************************************************")
	print("\tYou can now perform the following operations on this phonebook\n")
	print("1. Add a new contact")
	print("2. Remove an existing contact")
	print("3. Delete all contacts")
	print("4. Search for a contact")
	print("5. Display all contacts")
	print("6. Exit phonebook")
	choice = int(input("Please enter your choice: "))	
	return choice
def add_contact(pb):
	dip = []
	for i in range(len(pb[0])):
		if i == 0:
			dip.append(str(input("Enter name*: ")))
		if i == 1:
			dip.append(int(input("Enter number*: ")))
			if len(dip)!= 10:
					dip[i]=input("Contact no. should be 10 digits.")
		if i == 2:
			dip.append(str(input("Enter e-mail address: ")))
			if dip[i] !='':
					while "@" not in dip[i]:
						dip[i] = input("Your email address must have '@' in it\nPlease write your email address again : ")
						if "." not in dip[i]:
							dip[i]= input("Your email address must have '.' in it\nPlease write your email address again : ")
		if i == 3:
			dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
			if dip[i] !='':
					from datetime import datetime
					test_str = dip[i]
					format = "%d/%m/%Y"
					res = True
					try:
						res = bool(datetime.strptime(test_str, format))
					except ValueError:
						res = False
					if res == False :
						dip[i]=input("Invalid date format\nPlease enter valid date format : ")
					
		if i == 4:
			dip.append(str(input("Enter category(Family(F)/Friends(FR)/Work(W)/Others(O)): ")))
	pb.append(dip)
	return pb
def remove_existing(pb):
	contact  = str(input("Please enter the name of the contact you wish to remove: "))
	temp = 0
	for i in range(len(pb)):
		if contact  == pb[i][0]:
			temp += 1	
			print(pb.pop(i))
			print("This contact has now been removed")
			return pb
	if temp == 0:
		print("Sorry !, you have entered an invalid contact  or \n Please recheck and try again later.")		
		return pb
def delete_all(pb):
	return pb.clear()

def search_existing(pb):
	choice = int(input("Search choice\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. (Family(F)/Friends(Fr)/Work(W)/Others(O)\nPlease enter choice: "))
	temp = []
	check = -1
	if choice == 1:
		contact = str(input("Please enter the name of the contact you wish to search: "))
		for i in range(len(pb)):
			if contact  == pb[i][0]:
				check = i
				temp.append(pb[i])				
	elif choice == 2:
		contact  = int(
			input("Please enter the number of the contact you wish to search: "))
		for i in range(len(pb)):
			if contact  == pb[i][1]:
				check = i
				temp.append(pb[i])				
	elif choice == 3:
		contact  = str(input("Please enter the e-mail ID  or of the contact you wish to search: "))
		for i in range(len(pb)):
			if contact  == pb[i][2]:
				check = i
				temp.append(pb[i])				
	elif choice == 4:
		contact  = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)  of the contact you wish to search: "))
		for i in range(len(pb)):
			if contact  == pb[i][3]:
				check = i
				temp.append(pb[i])				
	elif choice == 5:
		contact  = str(input("Please enter the category of the contact you wish to search: "))
		for i in range(len(pb)):
			if contact  == pb[i][4]:
				check = i
				temp.append(pb[i])
	else:
		print("Invalid search criteria")
		return -1	
	if check == -1:
		return -1
	else:
		display_all(temp)
		return check
def display_all(pb):
	if not pb:
		print("Phonebook is empty: []")
	else:
		for i in range(len(pb)):
			print(pb[i])
def thanks():
	print("********************************************************************")
	print("Thank you for using our Smartphone directory system.")
	print("Please visit again!")
	print("********************************************************************")
	sys.exit("Goodbye, have a nice day ahead!")
print("....................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")
print("....................................................................")
ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
	ch = menu()
	if ch == 1:
		pb = add_contact(pb)
	elif ch == 2:
		pb = remove_existing(pb)
	elif ch == 3:
		pb = delete_all(pb)
	elif ch == 4:
		d = search_existing(pb)
		if d == -1:
			print("The contact does not exist.\n Please try again")
	elif ch == 5:
		display_all(pb)
	else:
		thanks()
