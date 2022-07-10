# Programming Assignment-2#
#Question-1#
Distance = float(input(" Please enter distance in kilometer :  "))
Mile = Distance/1.609
print(Mile)

#Question-2#
Temparature = float(input(" Please enter temparature in celcis :  "))
Temp_F = (Temparature*9/5)+32
print((Temp_F),"Faranite")

#Question-3#
import calendar
yy = int(input("Enter the year :  "))
mm = int(input("Enter the month :  "))
print(calendar.month(yy,mm))

#Question-4#
a =int(input(" Enter the value of a :  "))
b =int(input(" Enter the value of b :  "))
c =int(input(" Enter the value of c :  "))
X = (-b + ((b**2-4*a*c)**.5))/(2*a)
Y = (-b - ((b**2-4*a*c)**.5))/(2*a)
print(X)
print(Y)

#Question-5#
f = 10
e = 20
f,e=e,f
print("e ""=",e)
print("f ""=",f)