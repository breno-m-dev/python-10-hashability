# 3. Dictionary Keys

# Create a program that attempts to use each of the following objects as
# a dictionary key:

# objects = [
#     10,
#     "hello",
#     (1, 2),
#     [1, 2],
#     {1, 2},
#     {"a": 1}
# ]

# Your program should report something similar to:

# 10 -> can be used as a key
# "hello" -> can be used as a key
# [1, 2] -> CANNOT be used as a key
# ...
# Bonus

# Do not simply check the object's type. Determine whether it is usable 
# as a key based on Python's actual behavior.

import hash2

objects = [
    10,
    "hello",
    (1, 2),
    [1, 2],
    {1, 2},
    {"a": 1}
]

for i in objects:
    if hash2.is_hashable:
        print(f"{i} -> can be used as a key ")
    else:
        print(f"{i} -> CANNOT be used as a key ")