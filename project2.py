spring_points = 0
fall_points = 0
summer_points = 0
winter_points = 0


answer1 = input ("Do you perfer A short sleeves, B long sleeves, C tank tops, or D hoodie  ")
if answer1 == "A":
    spring_points+= 1 
elif answer1 =="B":
    fall_points = 1 
elif answer1 == "C":
    summer_points += 1
elif answer1 == "D":
    winter_points = 1


answer2 = input ("Do you perfer A worm  wether, B cold wether, C Hot weather, or D rainy weather?  ")
if answer2 == "A":
        spring_points += 1
elif answer2 == "B":
        fall_points += 1
elif answer2 =="C":
    summer_points += 1 
elif answer2 == "D":
    winter_points += 1 


answer3 = input (" would you rather A hike, B ski, C swim,or D stay in side  ")
if answer3 == "A" or answer3 == "B" :
    spring_points += 1
elif answer3 == "C" :
    fall_points += 1
    summer_points += 1 
elif answer3 == "D":
    winter_points += 1 

    print (f"Your score is { spring_points} winter, {fall_points} fall, {summer_points} summer, and {winter_points} winter")
if spring_points >fall_points and spring_points > summer_points:
     print(" you are a spring person")
elif winter_points > spring_points and winter_points > summer_points:
     print(" this shows your a winter person")
elif summer_points > fall_points and summer_points > spring_points:
     print(" you are a summer person")
     





