def sq_cube(numbers):
    """Return a list of lists containing both the square and the cube of only the even numbers in a given list. Must also be able to round the numbers to the nearest whole number

    Args:
        n (int): List or array like objects

    Return:
        array: square and cube of each even number in the list

    Egs:
        >>> sq_cube([50/2, 40/3, 30/4, 20/5, 10/6])
        [[64, 512], [16, 64], [4, 8]]
    """

    ro_list = [round(i) if type(i) == float else i for i in numbers] # round the floats
    
    sqcu_tuple = [(i ** 2, i ** 3) for i in ro_list if i % 2 == 0] # square and cube the even numbers
    
    sqcu_list = [list(tuple) for tuple in sqcu_tuple] # convert tuples into lists 
    
    # return the final list of squre and cubes
    return sqcu_list