txt = "welcome to the jungle"

x = txt.split()
new_String = ""
for i in range(0,len(x)):
    new_String = new_String + x.pop()
    new_String+=" "

print(new_String.strip())