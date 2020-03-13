import paramiko
import socket

commandlist = list[exit, lsusb, dmidecode -t1, sudo su]

Hostnamestr = str(input('Enter hostname\n'))
host = socket.gethostbyname(Hostnamestr)
try:
    #default PWD
    paramiko_ssh_client = paramiko.SSHClient()
    paramiko_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko_ssh_client.connect(hostname=host, username='Login', password='PWD', port=22, timeout=4)
    print('Connected!')
try:
    paramiko_ssh_client = paramiko.SSHClient()
    paramiko_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko_ssh_client.connect(hostname=host, username='login2', password='PWD2', port=22, timeout=4)
    print('Connected!')
except socket.timeout:
    print('ErrorOfConnect')
except socket.gaierror:
    print('unknown host')
except paramiko.ssh_exception.NoValidConnectionsError:
    print('Connection not run')
except TimeoutError:
    print('TimeoutError')
    
EnterCommand = int(input('Exit 0 press 0\n', 'randomcommand1 press 1\n', 'randomcommand2 press 2\n', 'randomcommand3 press 3\n', 'randomcommand4 press 4\n', ))
SentCommand = str(commandlist[EnterCommand])

if EnterCommand == 0:

    print('Logout and Exit!')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command('exit')
    paramiko_ssh_client.close()
    exit(0)
else:
    print('Run Command 1')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(SentCommand)
    data = stdout.read()
    result1 = data.decode('utf-8')
    print(result1)
    pass
