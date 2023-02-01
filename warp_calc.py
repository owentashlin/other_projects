#Warp Calculator
finished_length = input("What is the end length of your project? ")
fringe_length = input("How long will the fringe or hem be? ")
take_up = int(int(finished_length) + int(fringe_length))/10
loom_waste = input("What is your loom's average loom waste? ")
total_warp_length = int(finished_length) + int(fringe_length) + int(take_up) + int(loom_waste)
print(total_warp_length)