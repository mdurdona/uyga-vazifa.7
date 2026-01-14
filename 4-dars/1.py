# ------------------UYGA_VAZIFA--------------
# .----------1-MASALA--------.
# def matn(a):
#     a= a.split()
#     kupi = {}
#     max = 0
#     takrori = ""
#     for i in a:
#         if i in kupi:
#             kupi[i] +=1
#         else:
#             kupi[i] =1

#     for soz, son in kupi.items():
#         if son > max:
#             max = son
#             takrori = soz

#     print(takrori,max)

# text =  "olma nok olma gilos olma nok shaftoli"
# matn(text)

# .----------2-MASALA--------.
# def ballari(a):
#     jami = 0
#     soni = 0
#     for ism, fan in a.items():
#         for ball in fan.values():
#                 jami += ball
#                 soni +=1
#         orta = jami/soni        
#         print(f"{ism}:{orta}")

# students = {
#   "Ali": {"math": 90, "en": 80},
#   "Vali": {"math": 70, "en": 85}
#   }
# ballari(students)
# .----------3-MASALA--------.
# def products(a):
#     jami = 0
#     miqdor = []
#     for i in a:
#         miq = i["miqdor"]
#         jami += miq
#         miqdor.append(i)

#     miqdor = sorted(miqdor,key = lambda x:x["miqdor"])
#     eng_kamlari = miqdor[:3]
#     print("Umumiy mahsulot miqdori:",jami)
#     print("Eng kam qolgan 3 ta maxsulot : ", end = "")

#     for i in eng_kamlari:
#         print(i["mahsulot"], end = ",")

# ombor = [
#     {"mahsulot": "olma", "miqdor": 5},
#     {"mahsulot": "nok", "miqdor": 9},
#     {"mahsulot": "shaftoli", "miqdor": 7},
#     {"mahsulot": "anor", "miqdor": 4},
#     {"mahsulot": "banan", "miqdor": 6},
#     {"mahsulot": "uzum", "miqdor": 8},
#     {"mahsulot": "gilos", "miqdor": 2},
#     {"mahsulot": "tarvuz", "miqdor": 1},
#     {"mahsulot": "qovun", "miqdor": 3},
#     {"mahsulot": "limon", "miqdor": 5}
# ]
# products(ombor)


# .----------4-MASALA--------.
# def tartiblash(a):
#     for i, j in sorted(a.items(), key=lambda x: x[1]):
#        print(i)

# my_dict = {
#     "t": 3,
#     "p": 1,
#     "y": 2,
#     "o": 5,
#     "h": 4,
#     "n": 6,
# }
# tartiblash(my_dict)

# .----------5-MASALA--------.
# def unic(a):
#     individ = []
#     for i in a:
#        if i != "" and a.count(i) == 1:
#         individ.append(i)
#     print(individ)   
            
# mylist = ["olma", "", "olma", "gilos", ""]
# unic(mylist)
