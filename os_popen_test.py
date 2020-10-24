import os
import subprocess


cmd = "nvmekit show all | find Disk"
output = os.popen(cmd).read()[:6]
print(output)


'''
cmd = "nvmekit show all | find Disk"
cmd1 = "echo Cool"
process = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)

out, err = process.communicate()

print(out)
'''