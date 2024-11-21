# Step 1: Create an empty list
my_list = []
print(f"Step 1: {my_list}")

# Step 2: What does the list look like after appending elements 10, 20, 30, and 40?
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending 10, 20, 30, and 40: {my_list}")

# Step 3: What does the list look like after inserting 15 at the second position?
my_list.insert(1, 15)  # Insert 15 at index 1 (second position)
print(f"After inserting 15 at the second position: {my_list}")

# Step 4: What does the list look like after extending it with [50, 60, 70]?
my_list.extend([50, 60, 70])
print(f"After extending with [50, 60, 70]: {my_list}")

# Step 5: What does the list look like after removing the last element?
my_list.pop()
print(f"After removing the last element: {my_list}")

# Step 6: How does the list look after sorting it in ascending order?
my_list.sort()
print(f"After sorting in ascending order: {my_list}")

# Step 7: What is the index of the value 30 in the sorted list?
index_of_30 = my_list.index(30)
print(f"The index of 30 in the sorted list is: {index_of_30}")
