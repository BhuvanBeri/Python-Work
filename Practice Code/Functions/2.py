def paint_calc(height, width, cover) :
    number_of_cans = ((height * width) / cover)
    return round(number_of_cans)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5

total = paint_calc(height = test_h, width = test_w, cover = coverage)

print(f"You'll need {total} cans of paint.")
