import random
import string
import subprocess
import sys

def write_to_clipboard(output):
	process = subprocess.Popen(
		'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
	process.communicate(output.encode('utf-8'))

def main():
	password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(30)])
	write_to_clipboard(password)
	if len(sys.argv) > 1 :
		if sys.argv[1] == "--show_pwd":
			print password
	print 'New password copied to clipboard :)'


if __name__ == "__main__":
	if len(sys.argv) > 1 :
		if sys.argv[1] == "-h":
			print "Usage: python pass_gen.py [-show_pwd]"
			sys.exit(0)
	main()