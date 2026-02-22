with open("o.csv","r") as f:
    next(f)
    so = 1
    for line in f:
        data = line.strip().split(',')
        if so == 25:
            print(f"anh 25:{data}")
        if so == 14 or so == 19:
            print(f"anh {so}:{data}")
        if so in [23,11,4]:
            print(f"anh {so}:{data}")
        so += 1 