#!/usr/bin/python3
"""
    Lockboxes problem solution
"""


def canUnlockAll(boxes):
    """
        Returns a truthy value if all boxes in the array can opened
    """
    # check if boxes is a list
    if type(boxes) != list:
        return False

    unlocked_set = set()
    unlocked_set.add(0)

    for index, val in enumerate(boxes):
        # check if index box can't be unlocked
        if type(val) != list or not (index in unlocked_set):
            return False

        # add key indexes from unlocked box
        for elem in val:
            # go to each elem index and update the set
            if elem < len(boxes) and type(elem) == int:
                unlocked_set.update(boxes[elem])
        unlocked_set.update(val)

    return True
