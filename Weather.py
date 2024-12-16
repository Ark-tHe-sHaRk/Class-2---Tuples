Weather = (1, 0, 1, 0, 1, 1, 0)
sunny = 0
rainy = 0
for a in range(0, 7):
    if(Weather[a]==0):
        rainy += 1
    else:
        sunny +=1
if(sunny>rainy):
     print("It is good weather.")
else:
    print("It is not very good weather.")