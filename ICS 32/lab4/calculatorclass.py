# Creating a class for a simple/basic calcultator
class Calculator():
   #define my class variables
   __calcResult__ = 0
   #define my constructor for my calculator class
   def __init__(self):
      #initalize my class variables as part of my constructor
      self.__calcResult__ = 0
   #define getting/accessor method for getting result value
   def getResult(self):
      return self.__calcResult__
   #define setting/mutator method for setting the result value
   def setResult(self,result):
      self.__calcResult__ = result
   #define the method that performs addition
   def addNumbers(self, num1, num2):
      self.setResult(num1+num2)
   #define the method that performs the subtration
   def subNumbers(self,num1,num2):
      self.setResult(num1-num2)
   #define the method that performs the multiplication
   def mulNumbers(self, num1,num2):
      self.setResult(num1*num2)
   #define the method that perofrms division operation
   def divNumbers(self, num1, num2):
      self.setResult(num1/num2)
   #define the method that performs that correct operation
   def checkOperation(self,operation,num1,num2):
      if(operation == '+'):
         self.addNumbers(num1,num2)
      elif(operation == '-'):
         self.subNumbers(num1,num2)
      elif(operation == '*'):
         self.mulNumbers(num1,num2)
      elif(operation == '/'):
         self.divNumbers(num1,num2)
#Adding a if block to test my class
if __name__ == '__main__':
   #create a calculator object instance
   testCalc = Calculator()
   
   #confirm the class variables initialized
   print(testCalc.getResult())
   
   #Test the plus operation and print results
   testCalc.checkOperation('+',5,3)
   print(testCalc.getResult())
   
   #Test the plus operation and print results
   testCalc.checkOperation('-',5,3)
   print(testCalc.getResult())
   
   #Test the plus operation and print results
   testCalc.checkOperation('*',5,3)
   print(testCalc.getResult())
   
   #Test the plus operation and print results
   testCalc.checkOperation('/',5,3)
   print(testCalc.getResult())