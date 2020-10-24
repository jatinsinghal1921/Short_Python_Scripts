from jira import JIRA
from jira.exceptions import JIRAError
import json
import os

def login():

	cred_file = open("credentials.json","r")
	cred_dict = json.load(cred_file)

	options = {
	'server': 'https://cejira.sandisk.com'}

	try:
	    jira = JIRA(options = options, basic_auth = (cred_dict["user"],cred_dict["pass"]))
	except JIRAError as e:
	    if e.status_code == 401:
	        print("Login to JIRA failed. Check your username and password")

	print("done!")

	return jira


def download_attachments(jira,issue_name):

	issue = jira.issue(issue_name)
	attachments = issue.fields.attachment
	print(attachments)

	for attachment in attachments:
		file = attachment.filename
		extension = file.split(".")[1].strip()
		if (extension == "log") or (extension == "txt"): 
			writeFile = open(file,"wb") 
			writeFile.write(attachment.get())


def get_all_issues(jira,project):

	block_size = 5000
	block_num = 0
	while True:
		start_idx = block_num*block_size
		issues = jira.search_issues('project = ' + project, start_idx, block_size, assignee in ("39032"))
		if len(issues) == 0:
		    # Retrieve issues until there are no more to come
		    break
		block_num += 1
		for issue in issues:
			print(issue.key)
		    #log.info('%s: %s' % (issue.key, issue.fields.summary))

	
def createDir(dirName):

	try:
	    os.mkdir(dirName)
	    print("Directory " , dirName ,  " Created ") 
	except FileExistsError:
	    print("Directory " , dirName ,  " already exists")    


def main():

	jira = login()
	project = "CSSSYSVAL"
	createDir(project)
	os.chdir(project)

	# issue_name = "CSSSYSVAL-13166"
	# download_attachments(jira,issue_name)
	get_all_issues(jira,project)

main()