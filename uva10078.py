sampleInput1 = [[0, 0], [3, 0], [3, 3], [0, 3]]
sampleInput2 = [[0, 0], [3, 0], [1, 1], [0, 3]]


def ccw(p1, p2, p3):
    return ((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])) < 0.000001


def calc_cww(points):
    is_convex = False
    for i in range(len(points)-2):
        if ccw(points[i], points[i + 1], points[i + 2]):
            is_convex = True
            break
    print('Yes' if is_convex else 'No')


calc_cww(sampleInput1)
calc_cww(sampleInput2)

