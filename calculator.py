#Gabriel Crew
#Unit test in class activity

import unittest

def div(a,b):
  if b != 0:
    return(a / b)
  else:
    return("undefined")
def mul(a,b):
  return(a * b)
def sub(a,b):
  return(a - b)
def add(a,b):
  return(a + b)

print("What numbers would you like to test")
input_a = int(input("First number "))
input_b = int(input("Second number "))

print(str(input_a) + " + " + str(input_b) + " = " + str(add(input_a,input_b)))
print(str(input_a) + " - " + str(input_b)+ " = " + str(sub(input_a,input_b)))
print(str(input_a) + " * " + str(input_b)+ " = " + str(mul(input_a,input_b)))
print(str(input_a) + " / " + str(input_b)+ " = " + str(div(input_a,input_b)))

class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(add(5,7),12)
  def test2(self): self.assertEqual(sub(5,7),-2)
  def test3(self): self.assertEqual(mul(2,7),14)
  def test4(self): self.assertEqual(div(8,4),2)
  def test5(self): self.assertEqual(div(8,0),"undefined")
  def test6(self): self.assertEqual(div(0,4),0)
  def test7(self): self.assertEqual(mul(-8,4),-32)

if __name__ == '__main__':
  unittest.main()