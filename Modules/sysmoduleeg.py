import sys

#to get the input during the run time
print('Enter your input:')

print('Entered input is ',sys.stdin.readline())

n=len(sys.argv)

print('no of arguments',n)


print('first argument',sys.argv[0])

