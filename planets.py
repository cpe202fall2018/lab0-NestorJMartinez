def weight_on_planets():
   # write your code here
   weight = int(input("What do you weigh on Earth? "))
   marsW = weight * 0.38
   jupiterW = weight * 2.34
   print("On Mars you would weigh " ,marsW,  "\nOn Jupiter you would weigh " ,(jupiterW))
if __name__ == '__main__':
   weight_on_planets()