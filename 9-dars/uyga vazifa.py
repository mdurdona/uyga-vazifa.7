# -----------------------uyga vazifa 9.-----------
# ...........1-MISOL...........
# with open("uy 1-m.txt","r") as f:
#     a = f.read().split()
#     gap = ""
#     for  i in a:
#         gap += chr(int(i))

# with open("ascii.txt", "w") as f:
#     f.write(gap)        

# ...........2-MISOL...........
# with open("New.txt", "r") as f:
#     a = f.read().lower()
#     text = input("So`z kiriting:").lower()

#     if a.find(text) != -1:
#         print("Siz kiritgan so'z faylda bor.")
#     else:
#         print("Siz kiritgan so`z faylda mavjud emas.")

# ...........3-MISOL...........  
# with open("file1.txt","r") as f:
#     a = f.read()
#     katta = a.title() 
# with open("file1.txt","w")  as f:
#     f.write(katta)  

# ...........4-MISOL...........  
# with open("arifmetik.txt","r") as f:
#     a = f.read().split()
#     sum =0
#     for i in a:
#         sum+=int(i)
#     arifmetigi = sum/len(a)    
#     natija = round(arifmetigi)

# with open("arifmetik.txt","a") as f:
#     f.write("\n" + str(natija))
