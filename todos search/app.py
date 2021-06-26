import json

with open("todos.json") as file:
    r = json.load(file)

print("Nima bilan qidirmoqchisiz?\n"
      "userId-->1\n"
      "id-->2\n"
      "title-->3\n"
      "completed-->4")

choice = input("===>")

choice1 = input('Qidirilayatgan malumotni kiriting?\n-->')
a = []
for i in range(0, len(r)):
    if int(choice) == 1 and (int(choice1) == r[i]["userId"]):
        a.append(r[i])
    elif int(choice) == 2 and (int(choice1) == r[i]["id"]):
        a.append(r[i])
    elif int(choice) == 3 and (choice1 in r[i]["title"]):
        a.append(r[i])
    elif int(choice) == 4 and (choice1 in str(r[i]["completed"])):
        a.append(r[i])
# with open("new.json", 'w') as save:
#     s = json.dumps(save)
#
if len(a) == 0:
    print("False")
else:
    print(a)
