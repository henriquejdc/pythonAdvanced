import sys
import getopt


filename = "test.txt"
message = "Hello"


def myfunction(*args, **kwargs):
    print(args)
    print(kwargs)


myfunction('T1', 'T2', KEYONE=1, KEYTWO=2)


print(sys.argv)

# python3 parcing.py -m Hello World -f test.txt
opts, argus = getopt.getopt(sys.argv[1:], "f:m", ['filename', 'message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, "w+") as f:
    f.write(message)
