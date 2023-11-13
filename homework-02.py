#Renata Carlos Daou
#Nov 5, 2023
#Homework 2

birth = input ("Please, enter your year of birth ")
birth = int(birth)

#1) 
age= (2023 - birth)
print ("Your age is", age)

#2) average human heartbeat in a year is 35 million
heartbeat = age * 35
print("Your heart has beaten", heartbeat ,"million times")

#3) blue whale heart beats only twice per minute
#average blue whale heartbeat in a year is 10512000
whale = age * 10512000
print("A blue whale's heart has beaten", whale ,"times")

#4) 180 per minute
#average rabbit heartbeat in a year is 94608000
rabbit = age * 94608000
print (rabbit)
if rabbit > 1000000000:
        rabbitbillion = rabbit/ 1000000000
        print("A rabbit's heart has beaten", rabbitbillion ,"billion times")
else:
    print("A rabbit's heart has beaten", rabbit ,"times") 
    
#5 I just added the round funct
rabbit = age * 94608000
print (rabbit)
if rabbit > 1000000000:
        rabbitbillion = rabbit/ 1000000000
        print("A rabbit's heart has beaten", round(rabbitbillion,2) ,"billion times")
else:
    print("A rabbit's heart has beaten", rabbit ,"times") 
    
#6 
myage = 22
if age == myage:
    print("I don't know about you, but WE'RE feeling 22!!")
elif age > myage:
    diff = age - myage
    print("You're old. By", diff, "years.")
else:
    diff = myage - age
    print("You're young. By", diff, "years.")

    
#part 2 of 6
if (birth % 2) == 0:
    print("The birth year is even.")
else:
    print("The birth year is odd.")
    
#7 https://www.britannica.com/topic/presidency-of-the-United-States-of-America/Presidents-of-the-United-States
democrats = [1993, 1997, 2009, 2013, 2021]
presidents = 0
for year in democrats:
    if year >= birth:
        presidents += 1
print("here have been", presidents, "Democratic Party presidents since you were born")
    
#8
president = {
    1981: "Ronald Reagan",
    1989: "George H.W. Bush",
    1993: "Bill Clinton",
    2001: "George W. Bush",
    2009: "Barack Obama",
    2017: "Donald Trump",
    2021: "Joe Biden"
}

for key, value in president.items():
    if key == birth:
        print(f'The president is', value, 'in the year of', key)


#9 I am not sure what to do on the 8 question to make sure it gives a president for each year that the person might imput that is not the exact year that the president is in office
#I am getting the name of the president depending on the year with the dictionary!!

#10
if birth <= 2023:
    print ("Your age is", age)
else:
    print("You sure? That's the future bro")