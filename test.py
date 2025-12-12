#write a program to check if a movies suitable for a person based on their age and the movie rating category. Use (if,elif,else) statements.



age = int(input("Enter your age: "))
if age >= 18:
 print("You can watch any movies(including Adult-rated)")
elif age >= 13:
 print("You can watch PG-13 and lower-rated movies.")
elif age >= 7 and age < 13:
 print("You can watch G and PG-rated movies")
else:
 print("You should watch only G-rated(General Audience) movies")