def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    time = start
    dates = []
    while time < stop:
        dates.append(time)
        time += step

    total = 0
    for y in dates:
        total += f(y)*step
    return total
