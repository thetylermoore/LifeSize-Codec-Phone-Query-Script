import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

codec_list = [
	['1.1.1.1', 'Mock Store'],
	['1.1.1.1', 'Center Circle Conference Room'],
	['1.1.1.1', 'DC Footwear M&D'],
	['1.1.1.1', 'DC Great Wall'],
	['1.1.1.1', 'Exec Conf Room'],
	['1.1.1.1', 'Healy Office'],
	['1.1.1.1', 'IT Operations Room'],
	['1.1.1.1', 'IT War Room'],
	['1.1.1.1', 'Legal Tax Meeting Room'],
	['1.1.1.1', 'Mock Store'],
	['1.1.1.1', 'OT Office'],
	['1.1.1.1', 'QS Footwear M&D'],
	['1.1.1.1', 'QS M&D Pit'],
	['1.1.1.1', 'Roxy War Room'],
	['1.1.1.1', 'Center Circle Visitor Office'],
	]

#for row in codec_list:
#	print row[0]

for row in codec_list:

	try:
		ssh.connect(row[0], username='auto', password='lifesize')
	except paramiko.SSHException:
		print ("Connection Failed")
		quit()

	stdin,stdout,stderr = ssh.exec_command("get system phone-status")

	for line in stdout.readlines():
		print row[1] + " phone status " + line.strip()

#	stdin,stdout,stderr = ssh.exec_command("get system date")

#	for line in stdout.readlines():
#		print row[1] + " date verification " + line.strip()

	ssh.close()
