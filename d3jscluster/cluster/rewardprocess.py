import threading
import time
import os
class CheckThread(threading.Thread):
	def __init__(self, files):
		threading.Thread.__init__(self)
		self.files = files

	def check_reward(self,files):
		os.remove("./cluster/log/checklog.log")
		check_log = open('./cluster/log/checklog.log', 'a')
		check_log.write("hehehehhfffff\n")


	def run(self):
		self.check_reward(self.files)