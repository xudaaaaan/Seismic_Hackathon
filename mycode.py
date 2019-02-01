import json
import csv

data_path = "./Data/"

class DataObfuscator():
	def __init__():
		self.fake_file = data_path + "FakeInfo.csv"
		self.fake_info = None

	def read_file(filename):
		"""
		input: string (Json file name)
		output: list of python dictionary
		"""
		with open(data_path + filename, "r+") as f:
			return json.load(f)

	def output_file(info, filename):
		"""
		input:
		info: list of dictionary
		"""
		with open(data_path + filename, "w+") as f:
			json.dump(info, f)

	def fake_info():
		"""
		output: List[List of each line]
		"""
		with open(self.fake_file) as f:
			reader = csv.reader(f)
			info = list(reader)[1:]
			info = list(zip(*info))[1:] #3000 lines
			return info
			#sur, giv, mid, add, zipcode, email, username, phone, height, weight, dob, company, ssn


	def name_processor(ori_name):
		def hash_name(name):
			result = 0
			for char in name:
				result += ord(char)
			return (result % 3000)

		name = ori_name.split(" ")
		if len(name) == 3:
			f, m, l = hash_name(name[0]), hash_name(name[1]), hash_name(name[2])
		fake_first = self.fake_info[0][f]
		fake_last = self.fake_info[2][m]
		fake_mid = self.fake_info[2][l]
		return fake_first + fake_last + fake_mid
		

	def ID_processor(ori_id):
		

	def zip_processor(ori_zip):
		m = int(ori_zip) % 3000
		return self.fake_info[4]

	def SSN_processor(ori_ssn):
		pass

	def phone_processor(ori_phone):
		temp = str(ori_phone).split("-")
		district, res = temp[0], temp[1:].join("")
		fake_phone = self.fake_info[7][temp % 3000]
		return (district + fake_phone.split("-")[1:].join(" "))

	def email_processor(ori_email):
		def hash_email(email):
			result = 0
			for char in name:
				result += ord(char)
			return (result % 3000)
		return self.fake_info[5][hash_email(ori_email)]

	def company_processor(ori_company):
		pass

	def process_data(filename):
		self.read_file(filename)
		






