# 1. Write a function `make_dictionary` that takes two lists and returns a
# dictionary with the names as keys and the scores as values.

def make_dictionary(keys_list, values_list):
    new_dict = {}
    for i in range(len(keys_list)):
        key = keys_list[i]
        value = values_list[i]
        if key in new_dict:
            new_dict[key] += value
        else:
            new_dict[key] = value
    #new_dict[keys_list] = values_list
    return new_dict

# print(make_dictionary(["a", "b"], [1, 2]))
# print(make_dictionary([1, 2, 3], [5, 6, 7]))
# print(make_dictionary(["a", "b", "c", "b"], ["apple", "banana", "clementine", "date"]))
# print(make_dictionary(["key"], ["value"]))











# You have been given the following list fo students and their test scores:
names = ["Maria", "Nushi", "Mohammed", "Jose", "Wei"]
scores = [10, 23, 13, 18, 12]

# Assign the result of make_dictionary to score_dict, which will be used in the
# exercises that follow.
score_dict = make_dictionary(names, scores)

# 2. Using `score_dict`, find the score for "Nushi"
print(score_dict["Nushi"])

# 3. Add a score 19 for "John"
score_dict["John"] = 19
scores.append(19)

# 4. Calculate the average of all the scores in `score_dict`
##### pull scores, add together, divide 
y = 0
for i in scores:
    y += i
x = y/len(scores)
print(x)



# 5. Update the score for "Wei" to be 13
score_dict["Wei"] = 13

# 6. Nushi has just dropped this class. Delete "Nushi" and his score from
# `score_dict`
del score_dict["Nushi"]

print(score_dict)