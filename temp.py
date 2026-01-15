def doThing(data):
    count = 0
    for k in data:
        if data[k] > 50:
            count += 1

    if count > 1:
        return True
    return False
