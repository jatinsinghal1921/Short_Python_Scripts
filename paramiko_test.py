import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="10.66.85.60",username="sandisk",password="sandisk123")

stdin,stdout,stderr=ssh_client.exec_command("ls")
print(stdout.readlines())


ftp_client=ssh_client.open_sftp()
ftp_client.get("/home/sandisk/Desktop/CFGenc.fluf","C:\\Users\\39231\\Desktop")
ftp_client.close()