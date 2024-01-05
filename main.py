name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# String combines input of both names and then converts to lowercase.
combined_string = name1 + name2
lower_case_string = combined_string.lower()

# Counts the occurrences of the letters "t", "r", "u", and "e" in the combined string and calculates a value 'true' based on the counts.

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

# Counts the occurrences of the letters "l", "o", "v", and "e" to get value of 'love'
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

# Combines the values of 'true' and 'love' to create a score.
love_score = int(str(true) + str(love))

# Prints the love score using if, elif, and else.
if (love_score < 10) or (love_score > 90):
  print(
      f"Your love score is {love_score}, you go together like coke and mentos."
  )
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your love score is {love_score}, you are alright together.")
else:
  print(f"Your love score is {love_score}.")
