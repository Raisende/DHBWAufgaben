gros=int(input("Grose Tannenbaum bitte : "))
wiederholen=int(input("Wie oft ? : "))
if gros<3:
    gros=3

for i in range(0,gros):
    for p in range( wiederholen):

        for j in range((gros-1)-i) :
            print(" ",end="")
        for j in range((i*2)+1):
            print("*", end="")
        for j in range((gros) - i):
            print(" ", end="")

    print()

for i in range(2):

    for t in range(wiederholen):
        for j in range((gros-1)) :
            print(" ",end="")
        print("*", end="")
        for j in range((gros)) :
            print(" ",end="")

    print()

input()