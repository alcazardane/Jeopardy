def greet():
	print("Welcome to Jeoparty! A Jeopardy-inspired quiz game.")

def display():
	print("""
	Instructions for the game:
	 Every start of the round, you will have to choose one 
	 of the four categories and one of their five values: 
	  - Video Games (100, 200, 300, 400, 500)
	  - TV Show (100, 200, 300, 400, 500)
	  - Movies (100, 200, 300, 400, 500)
	  - Social Media (100, 200, 300, 400, 500)

	 When you already chose a category and a value,
	 a question will be flashed. If you got the question
	 correct, the question's value will be added to your 
	 total points. If you got the question wrong, the 
	 question's value will be deducted to your total points.

	 The process will repeat for ten rounds.
	 After the tenth round, if you reach or exceeds 
	 2,000 total points you will win the game, otherwise, 
	 you will lose.

	Goodluck!! 
				""")
	
def ask():
	print(input("Are you ready? Press any key ... "))