#Warp Calculator
finished_length = input("What is the end length of your project in inches? ")
fringe_length = input("How long will the fringe or hem be in in inches? ")
take_up = int(int(finished_length) + int(fringe_length)) / 10
loom_waste = input("What is your loom's average loom waste in inches? ")
total_warp_length = (round(int(finished_length) + int(fringe_length) + int(take_up) + int(loom_waste) / 12))
print(f'Total warp length: {total_warp_length}')

finished_width = input("What is the width of your finished project in inches? ")
total_width_on_loom = int(finished_width) + 1.5
print(f'Total width on loom: {total_width_on_loom}')

ends_per_inch = input("How many ends per inch will your project have? ")
total_warp_ends = int(total_width_on_loom) * int(ends_per_inch)
print(f'Total warp ends: {total_warp_ends}')

total_warp_needed = (round(int(total_warp_ends) * int(total_warp_length)) / 36)
print(f'Total yards of warp needed: {total_warp_needed}')

#Weft Calculator

weft_shot_length = int(int(total_width_on_loom) + int(total_width_on_loom) / 10)
print(f'Single weft shot length: {weft_shot_length}')

wefts_per_inch = input("What is the total wefts per inch? ")
inches_to_be_woven = int(finished_length) + int(fringe_length) + int(take_up)
total_weft_needed = (round(int(wefts_per_inch) * int(inches_to_be_woven)) / 36)
print(f'total yards of weft needed: {total_weft_needed}')