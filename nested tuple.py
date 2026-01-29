nested_tuple = ("apple", "banana", (10, 20, 30), [40, 50])

print(f"Nested tuple: {nested_tuple}")


nested_tuple_element = nested_tuple[2]
print(f"The nested tuple element is: {nested_tuple_element}")


value_30 = nested_tuple[2][2]
print(f"Accessing 30 from the nested tuple: {value_30}")

print("-" * 20) 
