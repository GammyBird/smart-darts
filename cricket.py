#------------------Board Value Constants--------------------

t20 = 60
d20 = 40
s20 = 20

t19 = 57
d19 = 38
s19 = 19

t18 = 54
d18 = 36
s18 = 18

t17 = 51
d17 = 34
s17 = 17

t16 = 48
d16 = 32
s16 = 16

t15 = 45
d15 = 30
s15 = 15

bull = 50
semi = 25

#-------------------------------------------Player 1 Score Calculations---------------------------------------------------

p1t20 = 0
p1d20 = 0
p1s20 = 0
p120 = 0

def score20p1():
    global p120
    p120 = 0 if (p1t20 * t20) + (p1d20 * d20) + (p1s20 * s20) <= 60 else ((p1t20 * t20) + (p1d20 * d20) + (p1s20 * s20)) - 60

#------------------------

p1t19 = 0
p1d19 = 0
p1s19 = 0
p119 = 0

def score19p1():
    global p119
    p119 = 0 if (p1t19 * t19) + (p1d19 * d19) + (p1s19 * s19) <= 57 else ((p1t19 * t19) + (p1d19 * d19) + (p1s19 * s19)) - 57

#--------------------------

p1t18 = 0
p1d18 = 0
p1s18 = 0
p118 = 0

def score18p1():
    global p118
    p118 = 0 if (p1t18 * t18) + (p1d18 * d18) + (p1s18 * s18) <= 54 else ((p1t18 * t18) + (p1d18 * d18) + (p1s18 * s18)) - 54

#---------------------------

p1t17 = 0
p1d17 = 0
p1s17 = 0
p117 = 0

def score17p1():
    global p117
    p117 = 0 if (p1t17 * t17) + (p1d17 * d17) + (p1s17 * s17) <= 51 else ((p1t17 * t17) + (p1d17 * d17) + (p1s17 * s17)) - 51

#----------------------------

p1t16 = 0
p1d16 = 0
p1s16 = 0
p116 = 0

def score16p1():
    global p116
    p116 = 0 if (p1t16 * t16) + (p1d16 * d16) + (p1s16 * s16) <= 48 else ((p1t16 * t16) + (p1d16 * d16) + (p1s16 * s16)) - 48

#-----------------------------

p1t15 = 0
p1d15 = 0
p1s15 = 0
p115 = 0

def score15p1():
    global p115
    p115 = 0 if (p1t15 * t15) + (p1d15 * d15) + (p1s15 * s15) <= 45 else ((p1t15 * t15) + (p1d15 * d15) + (p1s15 * s15)) - 45

#-----------------------------

p1bull = 0
p1semi = 0
p150 = 0

def scorebullp1():
    global p150
    p150 = 0 if (p1bull * bull) + (p1semi * semi) <= 75 else ((p1bull * bull) + (p1semi * semi)) - 75

#-----------------------------

p1total = p120 + p119 + p118 + p117 + p116 + p115 + p150

#--------------------------------------------Player 2 Score Calculations----------------------------------------------

p2t20 = 0
p2d20 = 0
p2s20 = 0

score20p2 = 0 if (p2t20 * t20) + (p2d20 * d20) + (p2s20 * s20) <= 60 else ((p2t20 * t20) + (p2d20 * d20) + (p2s20 * s20)) - 60

p2t19 = 0
p2d19 = 0
p2s19 = 0

score19p2 = 0 if (p2t19 * t19) + (p2d19 * d19) + (p2s19 * s19) <= 57 else ((p2t19 * t19) + (p2d19 * d19) + (p2s19 * s19)) - 57

p2t18 = 0
p2d18 = 0
p2s18 = 0

score18p2 = 0 if (p2t18 * t18) + (p2d18 * d18) + (p2s18 * s18) <= 54 else ((p2t18 * t18) + (p2d18 * d18) + (p2s18 * s18)) - 54

p2t17 = 0
p2d17 = 0
p2s17 = 0

score17p2 = 0 if (p2t17 * t17) + (p2d17 * d17) + (p2s17 * s17) <= 51 else ((p2t17 * t17) + (p2d17 * d17) + (p2s17 * s17)) - 51

p2t16 = 0
p2d16 = 0
p2s16 = 0

score16p2 = 0 if (p2t16 * t16) + (p2d16 * d16) + (p2s16 * s16) <= 48 else ((p2t16 * t16) + (p2d16 * d16) + (p2s16 * s16)) - 48

p2t15 = 0
p2d15 = 0
p2s15 = 0

score15p2 = 0 if (p2t15 * t15) + (p2d15 * d15) + (p2s15 * s15) <= 45 else ((p2t15 * t15) + (p2d15 * d15) + (p2s15 * s15)) - 45

p2bull = 0
p2semi = 0

scorebullp2 = 0 if (p2bull * bull) + (p2semi * semi) <= 75 else ((p2bull * bull) + (p2semi * semi)) - 75

p2total = score20p2 + score19p2 + score18p2 + score17p2 + score16p2 + score15p2 + scorebullp2

#--------------------End of Setup----------------------


def playerOneDartOne():
    global p1t20, p1d20, p1s20, p1t19, p1d19, p1s19, p1t18, p1d18, p1s18, p1t17, p1d17, p1s17, p1t16, p1d16, p1s16, p1t15, p1d15, p1s15, p1bull, p1semi
    
    p1d1 = int(input("Enter Dart #1: "))

    if p1d1 == t20:
        p1t20 += 1
        score20p1()
        print(p1t20)
        print(p120)
    elif p1d1 == d20:
        p1d20 += 1
        score20p1()
        print(p1d20)
        print(p120)
    elif p1d1 == s20:
        p1s20 += 1
        score20p1()
        print(p1s20)
        print(p120)
    elif p1d1 == t19:
        p1t19 += 1
        score19p1()
        print(p1t19)
        print(p119)
    elif p1d1 == t19:
        p1t19 += 1
        score19p1()
        print(p1t19)
        print(p119)
    elif p1d1 == d19:
        p1d19 += 1
        score19p1()
        print(p1d19)
        print(p119)
    elif p1d1 == s19:
        p1s19 += 1
        score19p1()
        print(p1s19)
        print(p119)
    elif p1d1 == t18:
        p1t18 += 1
        score18p1()
        print(p1t18)
        print(p118)
    elif p1d1 == d18:
        p1d18 += 1
        score18p1()
        print(p1d18)
        print(p118)
    elif p1d1 == s18:
        p1t18 += 1
        score18p1()
        print(p1s18)
        print(p118)
    elif p1d1 == t17:
        p1t17 += 1
        score17p1()
        print(p1t17)
        print(p117)
    elif p1d1 == d17:
        p1d17 += 1
        score17p1()
        print(p1d17)
        print(p117)
    elif p1d1 == s17:
        p1s17 += 1
        score17p1()
        print(p1d17)
        print(p117)
    elif p1d1 == t16:
        p1t16 += 1
        score16p1()
        print(p1t16)
        print(p116)
    elif p1d1 == d16:
        p1d16 += 1
        score16p1()
        print(p1d16)
        print(p116)
    elif p1d1 == s16:
        p1s16 += 1
        score16p1()
        print(p1s16)
        print(p116)
    elif p1d1 == t15:
        p1t15 += 1
        score15p1()
        print(p1t15)
        print(p115)
    elif p1d1 == d15:
        p1d15 += 1
        score15p1()
        print(p1d15)
        print(p115)
    elif p1d1 == s15:
        p1s15 += 1
        score15p1()
        print(p1s15)
        print(p115)
    elif p1d1 == bull:
        p1bull += 1
        scorebullp1()
        print(p1bull)
        print(p150)
    elif p1d1 == semi:
        p1semi += 1
        scorebullp1()
        print(p1semi)
        print(p150)

    else: print("Not a valid selection, please try again"), playerOneDartOne()

'''def playerOneDartTwo():
    global p1t20, p1d20, p1s20

    p1d2 = int(input("Enter Dart #2: "))

    if p1d2 == t20:
        p1t20 += 1
    elif p1d2 == d20:
        p1d20 += 1
    elif p1d2 == s20:
        p1s20 += 1
    else: print("Not a valid selection, please try again"), playerOneDartOne()

def playerOneDartThree():
    global p1t20, p1d20, p1s20
    
    p1d3 = int(input("Enter Dart #3: "))

    if p1d3 == t20:
        p1t20 += 1
    elif p1d3 == d20:
        p1d20 += 1
    elif p1d3 == s20:
        p1s20 += 1
    else: print("Not a valid selection, please try again"), playerOneDartOne()'''

playerOneDartOne()
playerOneDartOne()
playerOneDartOne()
playerOneDartOne()
playerOneDartOne()
playerOneDartOne()


      

#p1d2 = int(input("Enter Dart #2: "))
#p1d3 = int(input("Enter Dart #3: "))