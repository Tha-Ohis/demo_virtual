name= input('Enter your name:')
weight_pounds= float(input('Enter your weight:'))
weight_kg= (weight_pounds * 0.453592)
#(str(name)+" You weigh:"+str(weight_kg))
weight=(f"{name} You weigh: {weight_kg}")
print(weight)