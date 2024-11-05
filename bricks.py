def make_bricks(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - (5 * big)
    else:
        remainder = goal % 5
        
    return small >= remainder
print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))

