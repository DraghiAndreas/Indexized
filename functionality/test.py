def map_change_to_red(change):
    # clamp change to a max of -13
    change = max(change, -13)

    if change <= -0.5:
        start, end = (205,115,117), (225,95,97)
        frac = (abs(change) / 0.5)
    elif change <= -3:
        start, end = (225,95,97), (255,45,47)
        frac = (abs(change) - 0.5) / (3 - 0.5)
    elif change <= -13:
        start, end = (255,45,47), (140,0,0)
        frac = (abs(change) - 3) / (13 - 3)
    else:
        return (130/255,0,0)

    # interpolate each channel
    r = int(start[0] + frac * (end[0] - start[0]))
    g = int(start[1] + frac * (end[1] - start[1]))
    b = int(start[2] + frac * (end[2] - start[2]))

    print(r)

    map_change_to_red(-.14)