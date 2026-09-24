# 5. Create Your Own Unhashable Object

# Create a class:

# class Person:
#     ...

# and make its instances unhashable.

# The following should raise a TypeError:

# hash(person)
class Person1:
   
   def __init__(self, name) -> None:
      self.name = name
      pass
   def __eq__ (self, other):
       return self.name == other.name


test = Person1("Breno")
try:
    hash(test)
except Exception:
    print(f"{str(test.__class__)} UNHASHABLE")

class Person2:
   
   def __init__(self, name) -> None:
      self.name = name
      self.age = 26
      pass
   def __eq__ (self, other):
       return self.name == other.name
   def __hash__(self):
       return hash(self.name)

test = Person2("Breno")
test1 = Person2("Breno")
test.age = 27
print(test1.age)
print(test == test1)
try:
    hash(test)
    print(f"{str(test.__class__)} hashable ^_^")
except Exception:
    print(f"{str(test.__class__)} UNHASHABLE")


class Person3:
   hash = None
   def __init__(self, name) -> None:
      self.name = name
      pass
   def __eq__ (self, other):
       return self.name == other.name
   def __hash__(self):
       return hash(self.name)

test = Person3("Breno")
try:
    hash(test)
    print(f"{str(test.__class__)} hashable ^_^")
except Exception:
    print(f"{str(test.__class__)} UNHASHABLE")

class Person4:
   hash = None
   def __init__(self, name) -> None:
      self.name = name
      pass
   def __eq__ (self, other):
       return self.name == other.name


test = Person4("Breno")
try:
    hash(test)
    print(f"{str(test.__class__)} hashable ^_^")
except Exception:
    print(f"{str(test.__class__)} UNHASHABLE")

class Person5:
   
   def __init__(self, name) -> None:
      self.name = name
      __hash__ = None
      pass
   def __eq__ (self, other):
       return self.name == other.name
   def __hash__(self):
       return hash(self.name)

test = Person5("Breno")
try:
    hash(test)
    print(f"{str(test.__class__)} hashable ^_^")
except Exception:
    print(f"{str(test.__class__)} UNHASHABLE")

class Person6:
   
   def __init__(self, name) -> None:
      self.name = name
      __hash__ = 123
      pass
   def __eq__ (self, other):
       return self.name == other.name

test = Person6("Breno")
try:
    hash(test)
    print(f"{str(test.__class__)} hashable ^_^")
except Exception:
    print(f"{str(test.__class__)} UNHASHABLE")