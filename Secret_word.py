secret_word = "Barcelona"
guess = ""
count = 0
limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
  if count < limit:
    guess = input("Enter guess: ")
    count += 1
  else:
    out_of_guesses = True

if out_of_guesses:
  print("You lose")
else:
  print("You win")