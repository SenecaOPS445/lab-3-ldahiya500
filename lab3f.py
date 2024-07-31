#!/usr/bin/env python3
#AuthorID = lakshay2.@myseneca.ca
#Author = lakshay2

# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    new_item = ordered_list[-1] + 1 # this ensure that the new item is added at the last of the list by adding 1 from last item
    ordered_list.append(new_item) # this append the new item using .append

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for item in items_to_remove: # goes through all the items in the list
        while item in ordered_list: # while loop is used so all occurence of the item can be removed 
            ordered_list.remove(item) # this removes the item using .remove

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
