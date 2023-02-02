bill = input("what is the total amount of the bill? ")
party = input("how many members are in your party? ")

bill_int = int(bill)
party_int = int(party)

bill_port = (bill_int * 1.12) / party_int

print(round(bill_port, 2))