import paramiko

host = '10.11.1.99'
login = 'login'
sshpassword = 'password'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=login, password=sshpassword, port=port)
sftp_client = client.open_sftp()
remote_file = sftp_client.open('cred', 'r')
try:
	for line in remote_file:
		if 'OS_PASSWORD' in line:
			line = line.split('"')
			password = line[1]
			break
finally:
	remote_file.close()

print(password)
client.close()


"""
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=login, password=sshpassword, port=port)
stdin, stdout, stderr = client.exec_command('ls -l')
data = stdout.read() + stderr.read()
print(data.decode("utf-8"))
client.close()
"""