# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def ascending(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            temp = arr[i]
            
            if arr[i] > arr[j]:
                arr[i] = arr[j]
                arr[j] = temp
            
    return arr
    
def descending(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            temp = arr[i]
            
            if arr[i] < arr[j]:
                arr[i] = arr[j]
                arr[j] = temp
            
    return arr
    
test =	[30, 24,61,	12,	13,	20,	27,	22,	20,21,	30,	40,	41,	42,	40,	24] 

print(ascending(test))
print(descending(test))

