import random
import string
import subprocess
import argparse

def write_to_clipboard(password):
	process = subprocess.Popen(
		'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
	process.communicate(password.encode('utf-8'))
	print 'New password copied to clipboard :)'

def gen_pass(len):
	if len is None:
		len = 30
	password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(len)])
	return password

def show_pass(password):
	print password

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Generate strong passwords and copy it in clipboard. Characters used to generate the password are picked from these: " + string.ascii_letters + string.digits + string.punctuation)
	parser.add_argument('-s', '--show_pwd', help='show the password generated.', action='store_true')
	parser.add_argument('-d', '--disable_copy', help='disable the copy in the clipboard. note that using --disable_copy will automatically enable --show_pwd', action='store_true')
	parser.add_argument('-l', '--len', help='specify password length. (default is 30).', type=int)
	args = parser.parse_args()
	password = gen_pass(args.len)
	if args.disable_copy:
		args.show_pwd = True
	else:
		write_to_clipboard(password)
	if args.show_pwd:
		show_pass(password)
