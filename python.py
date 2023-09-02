#python identation
if 3>2:
    print('3 is greater than 2')

#python variables
x=5
y='hello world'
print(x,' ',y)
# casting
x=str(3) #output '3'
y=int(3) #output 3
z=float(3) #output 3.0
# variable names
myNameIs='waqar ahmad' #Camel Case
MyNameIs='waqar ahmad' #Pascal Case
my_name_is='waqar' # Sanke Case
#Assign Multiple values
x,y,z='orange','grapes','mango'
x=y=z='orange'
fruits=['orange','mango','grapes'] #list
#unpack collection
x,y,z=fruits
#output variable
print(x)
print(y)
print(z)
# global variable
x='ahmad'
def myfunc():
    print('waqar', x)
myfunc()
#local variable
name='ahmad'
def myfunc1():
    lastname='ahmad' #variabe inside a function is called local varibale
    print('waqar', lastname)
myfunc1()
print('waqar', name)
# global keyword
def myfunc2():
    global lastname
    lastname='ahmad'
myfunc2()
print ('my last name is: ',lastname)
