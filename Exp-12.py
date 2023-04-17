file =open("file.txt","r")
print(file.read)

file= open('txtfile.txt','w')
file.write("This is the WRite COmmand")
file.close()

file= open('txtfile.txt','a')
file.write(' this will add this line.')
file.close()