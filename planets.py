def weight_on_planets():
   # write your code here
   weight = int(input("What do you weigh on earth? "))
   marsW = weight * 0.38
   jupiterW = weight * 2.34
   print("\nOn Mars you would weigh" ,marsW,  "pounds.\nOn Jupiter you would weigh" ,jupiterW, "pounds.")
if __name__ == '__main__':
   weight_on_planets()