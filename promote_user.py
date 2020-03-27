python << END
import subprocess

subprocess.check_output('cd')

home_folder = subprocess.check_output('pwd')
subprocess.check_output(['sudo', 'dscl', '.', '-append', '/groups/admin', 'GroupMembership', '%s' % home_folder])

END
