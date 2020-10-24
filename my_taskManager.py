import os
import time
import sys
import ntpath


class my_taskManager:

	def __init__(self):
		self.whole_path = sys.argv[0]
		self.current_path, self.file_name = ntpath.split(self.whole_path)


	def getPID(self,process_name):
		self.processList_file = self.current_path + "\\process_list.txt"
		cmd = "tasklist > " + self.processList_file
		# cmd = "tasklist"
		os.system(cmd)
		# processList_file_obj = os.popen(cmd)
		time.sleep(1)

		required_pid_list = []
		start = 0
		processList_file_obj = open(self.processList_file,"r")
		lines = processList_file_obj.readlines()
		for line in lines:
			
			if line.find("============") > -1:
				start = 1
				continue

			if start == 1:
				process_array = line.split()
				process_name_inList = process_array[0]
				process_id = process_array[1]
				if(process_name in process_name_inList.lower()):
					required_pid_list.append(process_id)


		return required_pid_list


	def killProcess(self,process_name):
		
		pid_list = self.getPID(process_name)
		final_cmd = "taskkill"
		for pid in pid_list:
			final_cmd += " /PID " + pid

		print(final_cmd)
		os.system(final_cmd)


def main():
	tm_obj = my_taskManager()
	pid_list = tm_obj.getPID("firefox")

	# tm_obj.killProcess("firefox")


if __name__ == "__main__":
	main()
