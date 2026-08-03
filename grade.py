scores = list(
    map(
        int,
        input("Values: ").split()
    )
)
#print(scores)

for x in scores:
    if(x>=90):
        print ("Your grade is A, Wow! Excellent work!")
    elif(x>=80 and x<=89):
        print ("Your grade is B, Good job!") 
    elif(x>=70 and x<=79):
        print ("Your grade is C, You can do better!")
    elif(x>=60 and x<=69):
        print ("Your grade is D, You need to work harder!")
    else:
        print ("Your grade is F, You failed!, Trust me you can achive more, Don't give up!")    
