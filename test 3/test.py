# 8 kyu
# Age Range Compatibility Equation
def dating_range(age):
    if age > 14:
        min = int(age / 2 + 7)
        max = int((age - 7) * 2)
        return str(min) + "-" + str(max)
    else:
        min = int(age - 0.10 * age)
        max = int(age + 0.10 * age)
        return str(min) + "-" + str(max)
    
# 8 kyu
# Simple Fun #352: Reagent Formula
def isValid(formula):
    if 1 in formula and 2 in formula:
        return False
    elif 3 in formula and 4 in formula:
        return False
    elif 5 in formula and 6 not in formula:
        return False
    elif 6 in formula and 5 not in formula:
        return False
    elif 7 not in formula and 8 not in formula:
        return False
    else:
        return True
    
# 7 kyu
# Anagram Detection
def is_anagram(test, original):
    a = sorted(test.lower())
    b = sorted(original.lower())
    return "".join(a) == "".join(b)

# 7 kyu
# How many are smaller than me?
def smaller(arr):
    index = 0
    result = []
    for i in arr:
        index += 1
        num = 0
        for x in arr[index:]:
            if i > x:
                num += 1
        result.append(num)
    return result

# 6 kyu
# Unique In Order
def unique_in_order(sequence):
    if sequence == "" or sequence == [] or sequence == ():
        return []
    result = [sequence[0]]
    index = 1
    for i in sequence[1:]:
        if sequence[index - 1] != i:
            result.append(i)
        index += 1
    return result

