from easygui import *

class human:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    
    def modify_age(self, age):
        self.age = age
    
    def modify_height(self, height):
        self.height = height
        
    def modify_weight(self, weight):
        self.weight = weight
        
    def bmi(self):
        bmi = round(self.weight / (self.height * self.height), 2)
        return bmi

while True:
    try:
        person = multenterbox(msg='Add your personal information:', title='body index mass calculator', fields=['Name', 'Age', 'Gender', 'Height (meter)', 'Weight (kg)'])
        name = person[0]
        age = int(person[1])
        gender = person[2]
        height = float(person[3])
        weight = int(person[4])
    except ValueError:
        msgbox("Oh snap! you made an error, age, height and weight need to be numbers.")
        continue

    #Underweight = <18.5
    #Normal weight = 18.5~24.9 
    #Overweight = 25~29.9 
    #Obesity = BMI of 30 or greater
    print(person)
    data = human(name, age, gender, height, weight)
    bmi = data.bmi()
    msgbox('Your bmi is ' + str(bmi))
    if bmi <=18.5:
        msgbox('You are tooooooooooo skinny, you should eat more!!!')
    elif bmi >18.5 and bmi<24.9:
        msgbox('Congratulations! You dont have any problems.')
    elif bmi >25 and bmi<29.9:
        msgbox('Be careful, you are a bit overweight!')
    else:
        msgbox('Youre toooooooooooooo fat, should eat less and exersice more!!!')
    break
