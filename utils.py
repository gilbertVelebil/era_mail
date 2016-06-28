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