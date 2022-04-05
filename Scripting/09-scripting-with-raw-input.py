names = input('Enter the student names separated by comma(,):').split(',')# get and process input for a list of names
assignments = input('Enter assignments count separated by coma(,):').split(',') # get and process input for a list of the number of assignments
grades = input('Enter grades separated by coma(,):').split(',') # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for x in range(len(names)):
    print(message.format(names[x].strip().capitalize(), assignments[x], grades[x], str(int(grades[x]) + int(assignments[x])*2)))
    