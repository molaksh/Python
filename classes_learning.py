#
# Example file for working with classes
#

class Parent_class():
  def method1(self):
    print("method1")

  def method2(self, string1):
    print("method2 " + string1)

class Child_class(Parent_class):
  def method1(self):
    print("inside child class, method1")
    Parent_class.method1(self)
    print("exiting child class method1")

  def method2(self, string2):
    print("inside child class, method2")
    Parent_class.method2(self,"parent class call from child class method2")
    print("exiting child class method2")

def main():
  p = Parent_class()
  c = Child_class()

  # p.method1()
  # p.method2("parent class method 2 call")

  c.method1()
  c.method2("child class method 2 call")

  
if __name__ == "__main__":
  main()
  
  
