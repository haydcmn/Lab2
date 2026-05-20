#(a) 
#    def calculate_bmi(height, weight):
#    print("Height = " + height)
#    print("Weight = " + weight)

#     calculate_bmi(weight="57", height="1.73") */

#(b) 
#    def calculate_bmi(height, weight):
#    print("Height = " + height)
#    print("Weight = " + weight)
#
#    calculate_bmi(weight=57, height=1.73)

#(c)
#    def calculate_bmi(height, weight):
#    print("Height = " + str(height))
#    print("Weight = " + str(weight))

#    calculate_bmi(weight=57, height=1.73)

#(d)
#def calculate_bmi(height, weight):
#    print("Height = " + str(height))
#   print("Weight = " + str(weight))

#    bmi = weight / (height * height)

#    print("BMI = " + str(bmi))

#   if bmi < 18.5:
#        print("Under Weight")

#    elif bmi >= 18.5 and bmi <= 25:
#       print("Normal Weight")

#    else:
#        print("Over Weight")

#calculate_bmi(weight=57, height=1.73)

#(e)

def calculate_bmi(height, weight):
    bmi = weight / (height * height)
    
    if bmi < 18.5:
        return -1  # Under weight
    elif 18.5 <= bmi <= 25.0:
        return 0   # Normal weight
    else:
        return 1   # Over weight