amount=int(input("Enter theamount"))
premium_membership=input("Enter yes/no")
if amount>=1000 or premimum_membership=="yes":
    print("free delivery")
else:
    print("not a free delivery")