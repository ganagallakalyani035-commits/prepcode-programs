def check(balance,amount=5000):
  if amount%5000==0 and amount<=balance:
    return "allow"
  else:
    return "not allow"
result=check(20000,5000)
print(result)