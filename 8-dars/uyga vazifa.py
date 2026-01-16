# ************************UYGA VAZIFA*********
# ------------1-MISOL----------

# from datetime import date
# bugun = date.today()
# print(bugun.strftime("%d.%m.%Y"))

# ------------2-MISOL----------
# from datetime import date
# print("Tug`ilgan sanangizni kiriting")
# yil = int(input("Yil:"))
# oy = int(input("Oy :"))
# kun = int(input("Kun:"))

# tugilgan_sana = date(yil,oy,kun)
# now = date.today()

# farq = now - tugilgan_sana

# print(f"{farq.days} kun o`tdi ")


# ------------3-MISOL----------
# from datetime import date
# now = date.today()
# mustaqillik = date(now.year,9,1)
# if now > mustaqillik:
#     mustaqillik = date(now.year+1,9,1)

# qoldi = mustaqillik - now
# print(f"Keyingi mustqillik bayramiga {qoldi.days} kun qoldi")


# ------------4-MISOL----------
# A = [
#     [1, 2],
#     [3, 4]
# ]

# B = [
#     [5, 6],
#     [7, 8]
# ]


# C = [
#     [A[0][0] + B[0][0], A[0][1] + B[0][1]],
#     [A[1][0] + B[1][0], A[1][1] + B[1][1]]
# ]

# print(C)


# ------------5-MISOL----------
# from   translate  import Translator
# lst = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]

# tarjima =  Translator(to_lang="en",from_lang="uz")
# text = {}
# for i in lst:
#     if isinstance(i,str):
#         text[i] = tarjima.translate(i)
# print(text)        

# ------------6-MISOL----------

# filmlar = {
#     "Titanic": "Jack Dawson",
#     "Harry Potter": "Harry Potter",
#     "The Dark Knight": "Bruce Wayne (Batman)",
#     "The Matrix": "Neo (Thomas Anderson)",
#     "Forrest Gump": "Forrest Gump",
#     "Gladiator": "Maximus Decimus Meridius",
#     "Inception": "Dom Cobb",
#     "Spider-Man": "Peter Parker",
#     "Iron Man": "Tony Stark",
#     "The Lord of the Rings": "Frodo Baggins"
# }

# name = input("Film nomini kiriting:")
# try:
#     print(filmlar[name])
# except KeyError:
#     print("Bunday film yo`q")     
