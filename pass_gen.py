import random
import string
import subprocess

def write_to_clipboard(output):
	process = subprocess.Popen(
		'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
	process.communicate(output.encode('utf-8'))

random = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(30)])
write_to_clipboard(random)
print 'New password copied to clipboard :)'