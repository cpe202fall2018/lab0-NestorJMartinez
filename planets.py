def weight_on_planets():
   # write your code here
   print("What do you weigh on Earth?", end=' ')
   weight = input()
   marsW = weight * .38
   jupiterW = weight * 2.34
   print("On Mars you would weigh " + str(marsW) + "\nOn Jupiter you would weigh " + str(jupiterW))
   
if __name__ == '__main__':
   weight_on_planets()