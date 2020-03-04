#Written to remove specific preferred networks from student endpoints remotely via Mosyle MDM. 

#If you need to remove more than one network, just copy/paste line 7 and change the interface and SSID name paramaters as needed.
python << END
import subprocess

#Replace 'your-interface-name' and 'your-network-name' appropriately. Ie. en0 for interface and Teacher-WiFI for SSID name.  
subprocess.check_output(['sudo', 'networksetup', '-removepreferredwirelessnetwork', 'your-interface-name', 'your-ssid-name'])

END