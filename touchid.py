import subprocess

result = subprocess.check_output(['sudo', 'bioutil', '-w', '-s', '-u', '1'])

print(result)