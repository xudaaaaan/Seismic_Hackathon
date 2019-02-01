import json

class DataObfuscator():
	def __init__():


	def read_file(filename):
		"""
		input: string (Json file name)
		output: list of python dictionary
		"""
		with open(filename, "r+") as f:
			return json.load(f)

	def output_file(info, filename):
		"""
		input:
		info: list of dictionary
		"""
		with open(filename, "w+") as f:
			json.dump(info, f)
		return

	def name_processor(ori_name):
		pass

	def ID_processor(ori_name):
		pass

	def zip_processor(ori_zip):
		pass

	def SSN_processor(ori_ssn):
		pass

	def phone_processor(ori_phone):
		pass

	def email_processor(ori_email):
		pass

	def company_processor(ori_company):
		pass





