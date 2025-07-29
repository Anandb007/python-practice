'''name = "cat"
age = 2
country = "India"
studen = "no"
print (f"name: {name} \nage: {age} \ncountry: {country} \nstudent: {studen}")
################################################
name = input("Enter your name: ")
age = int(input("enter your age: " ))
student = input("you are a student yes/no: ")
student = student.lower() in ("yes", "y", "1", "true")
student = "yes" if student else "no"
print (f"your name is: {name} \nyour age is: {age} \nstudent status: {student}")
#################################################
x, y, z = 5, 10, 15
print(x)
print(y)
print(z)
x, y, z = y, z, x
print (f"x: {x}, y: {y}, z: {z}")
#################################################
project, year  = input ("enter your project name and year with speace: ").split()
year = int(year)
status = input ("do you have experience yes/no: ")
status = status.lower() in ("yes", "y", "true", "5")
status = "Yes" if status else "No"
experience = float(input("if you have an experiece then how many year: "))
print(f"project: {project}\nyear: {year}\nstatus: {status}\nexperience: {experience}")'''
##################################################
is_adult = input("Are you an adult? (yes/no): ")
has_ticket = input("Do you have a ticket? (yes/no): ")

is_adult_bool = is_adult.lower() in ("yes", "y", "true", "1")
has_ticket_bool = has_ticket.lower() in ("yes", "y", "true", "1")
print (f"AND result: {is_adult_bool and has_ticket_bool}")
print (f"or result: {is_adult_bool or has_ticket_bool}")
print (f"not result: { not has_ticket_bool}")
print (f"not result: { not is_adult_bool}")
