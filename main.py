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





















if __name__ == "__main__":
    main()
