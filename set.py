
# Adding an element
a={1,2,3}
a.add(4)
print(a)

#update() is used to add multiple items.

a={1,2,3}
a.update({4,5,6})
print(a)

# Removing the element

a={1,2,3}
a.remove(3)
print(a)

a={1,2,3}
a.pop() # The order of set is unordered, so we can't identify which element is popped. 
print(a)
