'''
Variable Assignment
'''

#Add 'Mannety' to the variable 'name'
# name = "Mannety"
# print(name)

#================

#assign same value to multiple variables on the same line
# a = b = c = 'cat'
# print(a)
# print(b)
# print(c)

#===============

#reuse variable names,the last assignment is printed
# colour = 'Red'
# colour = 'Blue'

# print(colour)

#================

#legal names
firstname = "John"
first_name = "John"
_firs_tname = "John"
firstName = "John"
firstname2 = "John"
FIRSTNAME = "John"

#illegal variable names
# 2firstname = "John"
# first-name = "John"
# first name = "John"

#=================
'''
Reserved Keywords
'''
help("keywords")

# from = "London"
# print(from)

#================

#variable types
# var = "Hello world"
# print(type(var))


# var = 23
# print(type(var))

'''
Object Identity
'''

# score = 400 
# print(id(score))
# print(identity)

#================

#score variable is saved into the pb by reference

# score = 400
# pb = score
# print(id(score))
# print(id(pb))

'''
Object Reference
'''

#both score and pb point to the same into object
#score ---------->int 100 <--------- pb

# score = 100
# pb = score

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)
 
# =================

#pb ----------> int 20
# score -----------> int 100
# pb = 20 
# score = 100

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

# ===================
# garbage collection

# pb  ----------> int 20 
# score ----------> str 'Completed'
#      ------------> int 100

# pb = 20 
# score = 100
# score = 'Completed'

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)




