import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="-i to ch!")
parse_object.add_option("-m","--mac",dest="mac_address",help="mac ch!")

print("Mac_changer Started!")

(user_inputs, arguments) = parse_object.parse_args()

user_interface = user_inputs.interface
user_mac_address = user_inputs.mac_address

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["ifconfig",user_interface,"up"])

