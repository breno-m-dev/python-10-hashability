# 2. The Suspicious Tuple

# Determine which of the following objects are hashable:

# a = (1, 2, 3)
# b = ("a", "b", "c")
# c = ([1, 2], [3, 4])
# d = (1, "hello", (2, 3))
# e = (1, {2, 3})

# Then write a function that explains why each object is or is not 
# hashable.

# Hint

# A tuple being immutable does not necessarily mean that every tuple is 
# hashable.
import itertools
a = (1, 2, 3)
b = ("a", "b", "c")
c = ([1, 2], {3, 4})
d = (1, "hello", (2, 3))
e = [1, {2, 3}]

test = [a, b, c, d, e]

def is_hashable(obj) -> bool:
    try:
        hash(obj)
    except Exception as e:
        return False
    return True

def why_not_hashable(obj) -> str:
    
    if isinstance(obj,(list, dict, set)):
        output ="Object not hashable because it is a "
        output += str(obj.__class__)
        return output
    
    output = "Object not hashable because it contains: "
    
    try:
        for i in obj:

            if isinstance(i, (list, dict, set)):
                output += str(i.__class__)
                output += " "
        return output


    except Exception:
        return "reason for object not being hashable is unkown"
def main():       
    for item in test:
        if(is_hashable(item)):
            print(f"{item} is hashable")
        else:
            
            print(f"{str(item)} {why_not_hashable(item)}")

if __name__ == '__main__':
    main()

