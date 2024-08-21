# Function to create an empty list
def create_an_empty_list():
    return []

# Function to create a list with specified elements
def create_a_list():
    return [1, 2, 3, 4]

# Function to add an element to the end of the list
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

# Function to add an element to the start of the list
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(lst):
    lst.pop()  # This removes the last element from the list
    return lst  # Return the modified list

def remove_element_from_start_of_list(lst):
    lst.pop(0)  # This removes the first element from the list
    return lst  # Return the modified list

# Function to retrieve the first element from the list
def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(lst, index):
    return lst[index]  # Return the element at the specified index

def retrieve_last_element_from_list(lst):
    return lst[-1]  # Return the last element of the list
