from netmiko import ConnectHandler
from getpass import getpass 
from datetime import datetime


device1 = {
    "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    ## "session_log": 'my_session.txt', 
}

device2 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    ## "session_log": 'my_session.txt', 
}

## net_connect = ConnectHandler(**device2)
## net_connect = ConnectHandler(**device1)

all_devices = [device1, device2]

start_time = datetime.now() 
for a_device in all_devices: 
    net_connect = ConnectHandler(**a_device) 
    output = net_connect.send_command("show version") 
with open ("output.txt", "a") as f: 
    print(f"\n\n--------- Device {a_device['device_type']} ---------", file=f) 
    print(output, file=f) 
    print("--------- End ---------", file=f) 
 
end_time = datetime.now() 
total_time = end_time - start_time  












