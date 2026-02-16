print("Hi")
name = input("What’s your name? \n")

print("Nice to meet you," ,name)
answer = input("Do you want the gold wash Or the classec wash?\n")

def wash_car ():
    if answer == "gold" :
        print ("the advantage of gold wash is")
        print ("1- wash with triple foam")
        print ("2- riense twice")
        print ("3- dry with large blow dryer")

    elif answer == "classec" :
        print ("the advantage of classec wash is")
        print ("1- wash with classec foam")
        print ("2- rience once")
        print ("3- air dry")

wash_car()

if answer == "gold" :
    answer1 = input("IT will cost 12$ \n")
    if answer1 == "ok" :
         print ("ok we will do it")
    elif answer1 ==  "noo" :
         print ("we can do classec")
         answer2 = input("can i give you the advantage of classec ? \n")
         if answer2 == "yes" :
            print ("1- wash with classec foam")
            print ("2- rience once")
            print ("3- air dry")
            print ("4- it will cost 6$")
            answer3 = input(" ok or no ?\n")
            if answer3 == "ok" :
                print ("ok we will do that")
            elif answer3 == "no" :
                print ("oh no i can’t do anything")    
         elif answer2 == "no" :
            print ("oh no i can’t do anything")            
         

elif answer == "classec" :
    answer4 = input ("IT will cost 6$ \n")
    if answer4 == "ok" :
         print ("ok we will do that")
    elif answer4 == "no" :
         print ("oh no i can’t do anything")     