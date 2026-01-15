def thing(data):
    for k in data:
        if data[k] < 60:
            print("FAIL:", k)
        elif data[k] >= 90:
            print("WOW:", k)
        else:
            pass
