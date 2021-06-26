import time
from pygame import mixer

mixer.init()
mixer.music.load("1122.mp3")
mixer.music.play(5)

time.sleep(5)
mixer.music.pause()
print('Call centirga xush kelibsiz!!!!!!!!\n'
      "Aperator bilan gaplashnoqchi bulsangiz 1-bosing\n"
      'Call centir xaqida malumot olmoqchi bulsangiz 2-bosing\n'
      'Kalkulayatordan foydalanmoqchi bulsangiz 3-bosing')
choise = int(input("--->"))


def aperator():
    mixer.music.play()
    time.sleep(5)
    mixer.music.stop()
    print("Matn kiriting", sep="\n")

    p = input("-->")
    d = ''
    for i in range(len(p) - 1, -1, -1):
        d = d + p[i]
    print(d)


def call():
    print("call center haqida malumot olish!!!\n"
          "kim tomonidan tuzilganligini bilish uchun 1-bosing\n"
          "call center uzi haqida malumot uchun 2-bosing\n"
          "takliflaringiz bulsa yozib qoldiring 3-bosing")
    j = int(input("===>"))
    a1 = True
    while a1:
        if j == 1:
            a1 = False
            print("Hamroyev Bobir Bahodirovich")
        elif j == 2:
            a1 = False
            print("call senterning asosiy xizmati bu kalkulyator")
        elif j == 3:
            a1 = False
            taklif = []
            b = input("takliflar --> ")
            taklif.append(b)
            print(b, "-taklifingizni qabul qilding!!!")
        else:
            print("Bazada yuq qiymat kiritdingiz")
            j = int(input("===>"))


def calculyator():
    """Bu dasdur bilan matematik amallreni bajaramiz"""

    a = float(input('son-->'))

    while True:
        c = input("amal kiriting->>")
        if c != '=':
            b = float(input('son-->'))
            if c == '+':
                a = a + b
            elif c == '-':
                a = a - b
            elif c == '*':
                a = a * b
            elif c == '/':
                a = a / b
            elif c == '//':
                a = a // b
            elif c == '**':
                a = a ** b
            elif c == 'i':
                a = a ** (1 / b)
            print(a)
        elif c == '=':
            print(a)
            break
        else:
            print("xato amal kiritdingiz")


if __name__ == '__main__':
    if choise == 1:
        aperator()
    elif choise == 2:
        call()
    elif choise == 3:
        calculyator()
    else:
        print('xato amal kiritdingiz')
    o = input("Amalbajarishni xoxlaysizmi (yes/no)")
    while 'yes' in o:
        choise = int(input("--->"))
        if choise == 1:
            aperator()
            e = False
        elif choise == 2:
            call()
            e = False
        elif choise == 3:
            calculyator()
            e = False
        else:
            print('xato amal kiritdingiz')
        o = input("Amalbajarishni xoxlaysizmi (yes/no)-->")
    else:
        print("Xizmatdan foydalanganingiz uchun raxmat!!!!!!!!")
