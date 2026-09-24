# 4. The Mutable Hashable Object

# Create your own class:

# class Person:
#     pass

# Create an instance and add it to a set:

# breno = Person()

# people = {breno}

# Then modify several attributes:

# breno.name = "breno"
# breno.age = 25

# Check whether:

# breno in people

# still works.

# Also investigate:

# hash(breno)

# before and after modifying the attributes.

# Questions
# How can an object be mutable and still be hashable?
# What determines the default hash of an instance of a user-defined 
# class? Does modifying an attribute necessarily change its hash?