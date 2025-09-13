#endswith() returns true if the string ends with specified value similar for startwith()

a="Saswajit Parida"
# print(a.endswith("a"))
# print(a.endswith("r",10,12))
# print(a.startswith("S"))
# print(a.startswith("P",9,13))

#swap case, lower case become upper case and vicecersa
print(a.swapcase())
#split() -splits the string at the specified opertor
# b="#oofd#Bgmd#h123"
# print(b.split("#"))

#ljust() returns a left justified version of the string similar for rjust()

a="Harry Porter"
x=a.ljust(20,"*")
#print(x,"is my favourite movie")
y=a.rjust(20,"-")
#print(y,"is my favouite movie")
b="my name is golu"
#print(b.replace("golu","Bitun")) #replace() is used to replace one word with other
# rindex()-searches the string for a specified value and returns the last positon where it is found same for rfind()
print(b.rindex("golu"))


# string slicing---------------
c="Harry Potter and the Goblet of fire"
# print(c[0:5])
# print(c[-4:])
#d=input("enter anything here")
#print(sorted(d))

e="saswajit"
#print(e.replace("s",""))

f="she sells seashells on the sea shore "
print(f.count("sea"))