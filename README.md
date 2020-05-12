usage: pass_gen.py [-h] [-s] [-d] [-l LEN]

Generate strong passwords and copy it in clipboard. Characters used to
generate the password are picked from these: abcdefghijklmnopqrstuvwxyzABCDEFG
HIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

optional arguments:
  -h, --help          show this help message and exit
  -s, --show_pwd      show the password generated.
  -d, --disable_copy  disable the copy in the clipboard. note that using
                      --disable_copy will automatically enable --show_pwd
  -l LEN, --len LEN   specify password length. (default is 30).