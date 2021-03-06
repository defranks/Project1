import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
today_date = date.today()

def getData(file):
	input = open(file, "r")
	input1 = input.readlines()[1:]
	input.close()
	lis = []


	for line in input1:

		dict = {}
		values = line.split(",")
		firstname = values[0]
		lastname = values[1]
		email = values[2]
		claass = values[3]
		dob = values[4]
		dict['First'] = firstname
		dict['Last'] = lastname
		dict['Email'] = email
		dict['Class'] = claass
		dict['DOB'] = dob
		lis.append(dict)

	return lis
	pass

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	newlist = sorted(data, key = lambda x: x[col])
	dictionary = newlist[0]
	first_name = dictionary["First"]
	last_name = dictionary["Last"]
	end_result = str(first_name + " " +  last_name)
	return end_result
	pass


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
	senior = 0
	junior = 0
	soph = 0
	fresh = 0
	for x in data:
		if x["Class"] == 'Senior':
			senior = senior + 1
		elif x["Class"] == 'Junior':
			junior = junior + 1
		elif x["Class"] == 'Sophomore':
			soph = soph + 1
		elif x["Class"] == 'Freshman':
			fresh = fresh + 1
	snr = ("Senior", senior)
	jnr = ("Junior", junior)
	sph = ("Sophomore", soph)
	frs = ("Freshman", fresh)
	list = [snr, jnr, sph, frs]
	sorted_list = sorted(list, key = lambda x: x[1], reverse = True)
	return sorted_list
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	pass


def findMonth(a):
# Find the most common birth month form this data

# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	list = []
	for x in a:
		z = x['DOB']
		r = z.split("/")
		list.append(r[0])
	mode = max(set(list), key=list.count)
	print(list)
	print(mode)
	return int(mode)

	pass

def mySortPrint(a,col,fileName):
	outfile = open(fileName, 'w')
	newlist = sorted(a[0:], key = lambda x: x[col])
	for x in newlist:
		student_info = x['First'] + ',' + x['Last'] + ',' + x['Email']
		outfile.write(student_info + '\n')
	outfile.close()
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):

	list = []
	number_students = len(a) - 1

	currentyear = int(today_date.year)
	print(currentyear)

	for x in a[1:]:
		z = x['DOB']
		dob = z.split("/")
		student_year = int(dob[2])
		sub = currentyear - student_year
		list.append(sub)
	ages = sum(list)

	avg = round(ages / number_students)
	return avg

# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
