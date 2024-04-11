
# 1. Create a list called 'shopping_list' with the following items:
# eggs
# bread
# bananas
# biscuits
# milk
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]


# 2. Print the list to the screen
print("This is your shopping list: \n" + str(shopping_list))

# 3. Print the data type of 'shopping_list'
print(f"The data type of your shopping list is: {type(shopping_list)}")

# 4. Print the first item in the list
print("The first item in your list is " + shopping_list[0])

# 5. Print the last item in the list
print("The last item in your list is " + shopping_list[-1])

# 6. Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed
print("The second item is currently " + shopping_list[1])
shopping_list[1] = "rice"
print("The second item has now become " + shopping_list[1])

# 7. Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)
print("The length of the list is currently", len(shopping_list))
shopping_list.append("carrots")
print("The length of the list is now", len(shopping_list))

# 8. Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.
forgotten_items = ["toffee", "coffee"]
shopping_list.extend(forgotten_items)

# 9. Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
print("This is your current shopping list: \n" + str(shopping_list))

# 10. Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
shopping_list.remove("bananas")
print("This is your current shopping list: \n" + str(shopping_list))

# 11. Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'
shopping_list.pop()
print("This is your current shopping list: \n" + str(shopping_list))

# 12. Use the "append" method to add an item to your list
shopping_list.append("watermelon")
print("This is your current shopping list: \n" + str(shopping_list))

# 13. Find a way to add a list of items (i.e. more than item) to your list
extra_items = ["double cream", "lettuce"]
shopping_list.extend(extra_items)
print("This is your current shopping list: \n" + str(shopping_list))

# 14. Use the "remove" method to remove an item from your list
shopping_list.remove("lettuce")
print("This is your current shopping list: \n" + str(shopping_list))

# 15. Find a way to remove the last item from the list (without referencing it)
shopping_list.pop()
print("This is your current shopping list: \n" + str(shopping_list))
