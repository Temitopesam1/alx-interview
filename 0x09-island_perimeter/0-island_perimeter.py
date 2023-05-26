#!/usr/bin/python3
'''Island perimeter module
'''


def island_perimeter(grid):
    '''Function to get an island perimeter
    Args:
        grid: A list of lists
    returns:
        perimetor or None if error
    '''
#     grid_dup = []
#     length = 0
#     breadth = 0

#     for item in grid:
#         if 1 in item:
#             grid_dup.append(item)
#     if len(grid_dup) == 0:
#         return None
#     for i in range(len(grid_dup)):
#         grid_dup[i] = grid_dup[i][1:-1]
#     get_length = sorted(grid_dup, reverse=True)
#     for item in get_length[0]:
#         if item == 1:
#             length += item
#     for item in get_length:
#         breadth += item[0]
#     return 2 * (length + breadth)
    count = 0
    for elem in grind:
        for item in elem:
            if item == 1:
                counter += item
    counter += 1
    return 2 * counter
