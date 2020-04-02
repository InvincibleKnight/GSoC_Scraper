import re, csv, json

def run():

	csv_file = "output.csv"

	json_file = "students.json"

	with open(csv_file) as f:
		csv_data = f.read()

	csv_data = list(csv.DictReader(csv_data.splitlines()))
	csv_data = check_for_non_official_names(csv_data)

	with open(json_file) as f:
		json_data = json.load(f)

	comparable_data = {}
	for student in json_data:
		comparable_data[student['n']] = {
			'roll_no': student['i'],
			'branch': student['d']
		}

	print("\nThe combined data is as follows:")
	print()
	for row in csv_data:
		if row['name'] in comparable_data:
			student_info = comparable_data[row['name']]
			print((f"Name:{row['name']}, Roll Number:{student_info['roll_no']}, "
				f"Branch: {student_info['branch']}, Project: {row['project']}, "
				f"Organization: {row['organization']}\n"))
		

def check_for_non_official_names(data):
	santised_data = []
	unoffical_names = []

	for row in data:
		name = row['name']
		if not re.match(r'^[A-Za-z\s]+$', name):
			unoffical_names.append(name)
		elif len(name.split()) < 2:
			unoffical_names.append(name)
		elif not re.match(r'[A-Z]+', name):
			unoffical_names.append(name)
		else:
			santised_data.append(row)

	return santised_data



if __name__ == "__main__":
	run()