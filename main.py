import random
heads = 0
tails = 0

f = ("Heads", "Tails")
for x in range (int(input("number of flips: "))):
  flip = random.choice(f)
  if flip == "Heads":
    heads += 1
  if flip == "Tails":
    tails += 1
  print(flip)

print("Heads: " + str(heads))
print("Tails: " + str(tails))

input("Press enter to Close:")