def compare_data_structures():
    # Lists
    list_example = [1, 2, 3, 4]
    
    # Tuples
    tuple_example = (1, 2, 3, 4)
    
    # Sets
    set_example = {1, 2, 3, 4}
    
    # Dictionaries
    dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    
    # Comparing pros and cons
    print("Lists:")
    print("Pros:", "Mutability, indexing, slicing, ordered")
    print("Cons:", "Slower lookup, memory overhead")
    print("\nTuples:")
    print("Pros:", "Immutable, indexed, sliced, memory-efficient")
    print("Cons:", "Slower than lists for modification, less versatile")
    print("\nSets:")
    print("Pros:", "Uniqueness, fast membership testing, set operations")
    print("Cons:", "Unordered, not indexed, cannot contain duplicates")
    print("\nDictionaries:")
    print("Pros:", "Key-value pairs, fast lookups, versatile")
    print("Cons:", "Unordered (prior to Python 3.7), memory overhead, keys must be hashable")

# Call the function to compare data structures
compare_data_structures()
