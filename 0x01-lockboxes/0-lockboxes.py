#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    count = 0

    while count < length:
        old_count = count
        opened_boxes.append(count)
        keys.update(boxes[count])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                count = key
                break
        if old_count != count:
            continue
        else:
            break

    for val in range(length):
        if val not in opened_boxes and val != 0:
            return False
    return True
