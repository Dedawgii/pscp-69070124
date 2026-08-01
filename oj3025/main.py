"""[LEARNING LOGS] Season"""

def main():
    """main"""
    M = int(input())
    D = int(input())
    if M in [1,2,3]:
        if M == 3 and D >= 21:
            print("spring")
        else:
            print("winter")
    if M in [4,5,6]:
        if M == 6 and D >= 21:
            print("summer")
        else:
            print("spring")
    if M in [7,8,9]:
        if M == 9 and D >= 21:
            print("fall")
        else:
            print("summer")
    if M in [10,11,12]:
        if M == 12 and D >= 21:
            print("winter")
        else:
            print("fall")

main()
