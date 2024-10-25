from time import process_time_ns

values = [1, 2, "alberto", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0]) # 1
print(values[3]) # 4
print(values[-1]) # 5
print(values[1:3]) # 2 "alberto"
values.insert(3, "anguiano") # insert element on the index 3
values.append("End") # Add element at end of the array
values[3] = "valdivia" # updating
del values[0] # deleted the first element
print(values) # [2, 'alberto', 'valdivia', 4, 5, 'End']
