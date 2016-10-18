from traceback import format_tb
from sys import exc_info
import os

def exceptTraceback(excpt):
    return [excpt,format_tb(exc_info()[2])]

def absFilePath(rel_path):
	"""
	constructs absolute path based on relative path and the script directory
	"""
	script_dir = os.path.dirname(__file__)
	return os.path.join(script_dir, rel_path)

def readTabbedFile(file_nm):
	"""
	read and parse a text file
	return a list of [login name, password]
	"""
	tabbed_list = []
	try:
		with open(file_nm,'r') as f:
			content_split = f.read().split()
			for i in content_split:
				tabbed_list.append(i.strip())		
		# return [content_split[0].strip(),content_split[1].strip()]
		return tabbed_list
	# except FileNotFoundError:
	# 	return []
	except Exception as e:
		raise Exception(e)