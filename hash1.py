# Hashables in Python — Practice Exercises

# A set of exercises designed to develop a deeper understanding of
# hashable objects, hash functions, mutability, dict, set, __eq__,
# and __hash__.

# The exercises are ordered from basic concepts to custom hashable objects.

# 1. The Hashable Detector

# Create a function:

# def is_hashable(obj):
#     ...

# The function should receive any Python object and return:

# True

# if the object is hashable, and:

# False

# otherwise.

# Test it with:

# 42
# 3.14
# "Julia"
# [1, 2, 3]
# (1, 2, 3)
# {"a": 1}
# {1, 2, 3}
# Goal

# Understand how to determine whether an object is hashable based on 
# Python's actual behavior rather than simply checking its type.

def is_hashable(obj):
    try:
        hash(obj)
    except Exception as e:
        return False
    return True


test = [42, 3.14, "Julia", [1, 2, 3], (1, 2, 3), {"a":1}, {1,2,3}]

for item in test:
    if(is_hashable(item)):
        print(f"{item} is hashable")
    else:
        print(f"{item} is NOT hashable")