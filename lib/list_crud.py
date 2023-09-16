def create_an_empty_list():
    return []

def create_a_list():
    return ['a', 'b', 'c', 'd']

def add_element_to_end_of_list(lst, element):
    lst.append(element)
    return lst

def add_element_to_start_of_list(lst, element):
    lst.insert(0, element)
    return lst

def remove_element_from_end_of_list(lst):
    if lst:
        lst.pop()
    return lst

def remove_element_from_start_of_list(lst):
    if lst:
        del lst[0]
    return lst

def retrieve_first_element_from_list(lst):
    if lst:
        return lst[0]

def retrieve_element_from_index(lst, index):
    if 0 <= index < len(lst):
        return lst[index]

def retrieve_last_element_from_list(lst):
    if lst:
        return lst[-1]