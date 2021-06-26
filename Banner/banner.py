"""biz banneryasash kodini yozdik biz buni bajarishda 5ta listdan va
bitta lug'at listidan foydalandik,faqat etiboli bo'linhg harflarimiz cheklangan"""
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

dict1 = {
    'a': [
        "    ##    ",
        "   #  #   ",
        "  ######  ",
        " #      # ",
        "#        #"
    ],
    'b': [
        "###### ",
        "#     #",
        "###### ",
        "#     #",
        "#######"
    ],
    'd': [
        "####### ",
        "#      #",
        "#      #",
        "#      #",
        "####### "
    ],
    'e': [
        "#######",
        "#      ",
        "#####  ",
        "#      ",
        "#######"
    ],
    "o": [
        " ##### ",
        "#     #",
        "#     #",
        "#     #",
        " ##### "
    ],
    "i": [
        "######",
        "  ##  ",
        "  ##  ",
        "  ##  ",
        "######"
    ],
    "r": [
        "###### ",
        "#     #",
        "###### ",
        "#  #   ",
        "#    # "
    ]

}
a = input("Matn kiriting-->").lower()
c = input("Og'ma shirf chiqarishni xoxlaysizmi?(yes/no)").lower()
if c in 'yes':
    q = input("right-hand or left-hand?(righ/left)").lower()
    if q in "right":
        list1.append('    ')
        list2.append('   ')
        list3.append('  ')
        list4.append(' ')
        list5.append('')
    else:
        list5.append('    ')
        list4.append('   ')
        list3.append('  ')
        list2.append(' ')
        list1.append('')
while True:
    b = input("belgi kiriting-->")
    if len(b) == 1:
        for i in range(0, len(a)):
            list1.append(dict1[a[i]][0].replace("#", b))
            list2.append(dict1[a[i]][1].replace("#", b))
            list3.append(dict1[a[i]][2].replace("#", b))
            list4.append(dict1[a[i]][3].replace("#", b))
            list5.append(dict1[a[i]][4].replace("#", b))
        print(list1, list2, list3, list4, list5, sep='\n')
        break
    else:
        print("Siz xato qiymat kiritdingiz (Bittadan kup belgi kiritish mumkin emas!!!)")


# n = int(input("-->"))
# list1 = [1, 2]
# while n > len(list1):
#     list1.append(list1[len(list1) - 2] + list1[len(list1)-1])
# print(list1)
