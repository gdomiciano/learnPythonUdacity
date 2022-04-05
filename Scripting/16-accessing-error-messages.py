#When you handle an exception, you can still access its error message like this:

try:
   90 // 0
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
#This would print something like this:

#ZeroDivisionError occurred: integer division or modulo by zero
#So you can still access error messages, even if you handle them to keep your program from crashing!

#If you don't have a specific error you're handling, you can still access the message like this:

try:
    value
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))