#try:
    # write some code
    # that might throw exception
#except <ExceptionType>:
    # Exception handler, alert the user

try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('file not found')