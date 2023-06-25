import instructions as inst
import game as g

inst.greet()
inst.display()
inst.ask()


name = input("What is your name : ")
print("Welcome! "+ name + "!")


print("Choose a category : VIDEO GAMES || TV SHOWS || MOVIES || SOCIAL MEDIA")
categ = input("Ans: ")
print("Choose a value : 100 || 200 || 300 || 400 || 500")
q_value = input("Ans: ")

cv = g.gameClass(categ, q_value)
cv.categ_value()