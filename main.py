import paramiko
import socket
import time
import colorama
from colorama import Fore
colorama.init()
print(Fore.YELLOW + '')
Hostnamestr = str(input('Enter hostname\n'))
host = socket.gethostbyname(Hostnamestr)
try:
    #default PWD
    paramiko_ssh_client = paramiko.SSHClient()
    paramiko_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko_ssh_client.connect(hostname=host, username='Login', password='PWD', port=22, timeout=4)
    print(Fore.GREEN + 'Connected!')
    print(Style.RESET_ALL)
except socket.timeout:
    print(Fore.RED + 'ErrorOfConnect')
    print(Style.RESET_ALL)
except socket.gaierror:
    print(Fore.RED + 'unknown host')
    print(Style.RESET_ALL)
except paramiko.ssh_exception.NoValidConnectionsError:
    print(Fore.RED + 'Connection not run')
    print(Style.RESET_ALL)
except TimeoutError:
    print(Fore.RED + 'TimeoutError')
    print(Style.RESET_ALL)
try:
    # AlternativePWD
    paramiko_ssh_client = paramiko.SSHClient()
    paramiko_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko_ssh_client.connect(hostname=host, username='login2', password='PWD2', port=22, timeout=4)
    print(Fore.GREEN + 'Connected!')
    print(Style.RESET_ALL)
except socket.timeout:
    print(Fore.RED + 'ErrorOfConnect')
    print(Style.RESET_ALL)
except socket.gaierror:
    print(Fore.RED + 'unknown host')
    print(Style.RESET_ALL)
except paramiko.ssh_exception.NoValidConnectionsError:
    print(Fore.RED + 'Connection not run')
    print(Style.RESET_ALL)
except TimeoutError:
    print(Fore.RED + 'TimeoutError')
    print(Style.RESET_ALL)
#choose a command
print(Fore.YELLOW + 'Run Command 1 press 1')
print(Fore.YELLOW + 'Run Command 2 press 2')
print(Fore.YELLOW + 'Run Command 3 press 3')
print(Fore.YELLOW + 'Run Command 4 press 4')
print(Fore.RED + 'Logout and Exit press 0')

print(Fore.GREEN + '')
Whatismake = int(input('What do we do?\n'))
print(Fore.YELLOW + '*')
time.sleep(0.2)
print(Fore.YELLOW + '**')
time.sleep(0.2)
print(Fore.YELLOW + '***')
time.sleep(0.2)
print(Fore.YELLOW + '****')
time.sleep(0.2)
print(Fore.YELLOW + '*****')
time.sleep(0.2)
print(Fore.YELLOW + '******')
time.sleep(0.2)
print(Fore.YELLOW + '*******')
time.sleep(0.2)
print(Fore.YELLOW + '********')


#assign actions for command 1-4
if Whatismake == 1:
    print('Run Command 1')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command('lsusb')
    data = stdout.read()
    result1 = data.decode('utf-8')
    print(result1)
elif Whatismake == 2:
    print('Run Command 2')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command('init 6')
    data = stdout.read()
    result1 = data.decode('utf-8')
    print(result1)
elif Whatismake == 3:
    print('Run Command 3')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command('dmidecode -t1')
    data = stdout.read()
    result1 = data.decode('utf-8')
    print(result1)
elif Whatismake == 4:
    print('Run Command 4')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command('systemctl status cups.service')
    data = stdout.read()
    result1 = data.decode('utf-8')
    print(result1)
elif Whatismake == 0:
    print('Logout and Exit!')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command('exit')
    paramiko_ssh_client.close()
    exit(0)
else:
    print('Logout and Exit!')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command('exit')
    paramiko_ssh_client.close()
    exit(0)
    pass
