def main():
    
    my_list = ["p", "a", "n", "d", "a"]
    print(my_list)
    # What do you see? Record it here: i see ['p' 'a' 'n'...]
    my_list.append("!")
    print(my_list)
    # What changed? Describe the difference between the original and updated list:
    # now its like the same thing and adds " '!' " to the end
    print(len(my_list))
    # How many elements are there? Record it: 6
    print(my_list[4:6])
    # What values were returned? Why do those indexes work?
    # it returned the values of the 4th and 6th indexes.
    print(my_list[4:])
    # What do you notice? Is the result the same as above? - its the same result but the # other one is missing why?
    print(my_list[-2:])
    # What does this do? Why is it useful? - goes from the backwards, useful for very long # lists
    my_list.remove("d")
    print(my_list)
    # What changed? Where did it remove the "l" from? - removed index 4
    my_list.insert(2, "d")
    print(my_list)
    # Did it go where you expected? What is at index 2 now? yes, d went to i2
    del my_list[0]
    print(my_list)
    # What item got removed? - delets index 0 so the p
    last_item = my_list.pop()
    print(last_item)
    print(my_list)
    # What item was removed? What’s left in the list? - last item in index gets returned
    print(my_list[2])
    # What is it? 'n' which is index 2
    print("!" in my_list)
    # True or False? Why? False, because it was popped earlier
    my_list.sort(reverse=True)
    print(my_list)
    # What is the new order? Did sort() return anything? order is now in descending order of the alphabet
    print(sorted(my_list))
    print(my_list)
    # Did the original change? What’s the difference between sorted() and sort()?
    # its sorted to ascending order in the alphabet, but then it got changed back again



    my_tuple = ("red", "green", "blue")
    print(my_tuple)
    # What values are inside this tuple? - red g b
    print(my_tuple[0])
    print(my_tuple[-1])
    # What was printed in each case? Why does negative indexing work? - red and blue, it works and it goes backwards which is hella cool
    # my_tuple[1] = "yellow"
    # What happens? What error do you get? i get an object doesnt support assignment
    one_item = ("hello",)
    print(one_item)
    # What do you notice about the syntax? it included the comma but why? bc its a tuple
    colors = ("red", "blue", "red", "green", "red")
    print(colors.count("red"))
# How many "red" entries are there? - 3
    print(colors.index("green"))
# What position is "green" in the tuple? - 3


    my_set = {"apple", "banana", "cherry"}
    print(my_set)
# Does the order match what you typed? Why or why not? no, bc im not actually sure
    my_set.add("orange")
    print(my_set)
# What changed? - added orange to the front
    my_set.add("banana")
    print(my_set)
# Did anything change? Why or why not? no bc its a dupe so its overidden and kept the same
    my_set.remove("apple")
    print(my_set)
# Which item is gone? the apple
    my_set.discard("pear")
# What happened? Was there an error? - apple went to the front and now in alphabetical order but rfemoved it and now others changed pos
    tropical = {"banana", "mango", "papaya"}
    all_fruits = my_set.union(tropical)
    print(all_fruits)
# What items are in the result? Any duplicates?no dupes, added mango and papaya

    my_dict = {"name": "Sam", "age": 16, "grade": "11th"}
    print(my_dict)
# What keys and values are present? name age and grade and values are sam 16 11th
    print(my_dict["age"])
    # What value did this return? - 16 which is the value of the key age
    # print(my_dict["school"])
# What error do you get? key error bc theres no key - made it a comment so i can print latyer
    my_dict["grade"] = "12th"
    print(my_dict)
# Did the value update? yes
    my_dict["school"] = "Central High"
    print(my_dict)
# What’s the new key and value? - school and value of central high
    del my_dict["age"]
    print(my_dict)
# Which key is missing now? removed age key and value
    print(my_dict.get("locker"))
# What value was returned? Was there an error? no value
    for key, value in my_dict.items():
    print(key, "->", value)
# What got printed? How does this help you read the dictionary? - got errorS



































if __name__ == "__main__":
    main()
