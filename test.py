import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--len', help="echo the string you use here")
args = parser.parse_args()
print(args.len)