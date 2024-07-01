def are_arrays_equal(l1, l2):


    # Check if the sets are equal
    return sorted(l1) == sorted(l2)

# Example usage:
l1 = ['mickey', 'donald', 'goofy']
l2 = ['goofy', 'mickey', 'donald']
l3 = ['goofy', 'mickey', 'donald duck']

if are_arrays_equal(l1,l2):
    print("Arrays have the same values.")
else:
    print("Arrays do not have the same values.")