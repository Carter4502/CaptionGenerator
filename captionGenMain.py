import tkinter as tk
import random

userName = "instagramName"
def generateRandomName():
	good_consonants = list("bcdfghjklmnprst")
	vowels = list("aeiou")
	length = random.randint(4, 6)
	print(length)
	firstCons = random.choice(good_consonants)
	firstVowel = random.choice(vowels)
	vowels.remove(firstVowel)
	good_consonants.remove(firstCons)
	first = firstCons + firstVowel
	lastWasVowel = True
	endOfString = ""
	for x in range(length - 2):
		if lastWasVowel:
			cons = random.choice(good_consonants)
			good_consonants.remove(cons)
			endOfString = endOfString + cons
			lastWasVowel = False
		else:
			vow = random.choice(vowels)
			vowels.remove(vow)
			endOfString = endOfString + vow
			lastWasVowel = True
	numNumbers = random.randint(0, 5)
	finalString = first + endOfString
	for i in range(numNumbers):
		finalString = finalString + str(random.randint(0,9))
	return finalString

def createCap(root):
	randomUser = generateRandomName()
	capText = "\nfollow me @" + userName + " 📱\nfollow me @" + userName + " 💻\nfollow me @" + userName + " 🎧\n-\noriginal credit: " + randomUser + " (dm for\ncredits/removal)\n-\n-\n-"
	my_txt = tk.StringVar()
	my_txt.set(capText)
	captionBox = tk.Text(root, font=("arial", 12))
	captionBox.insert(1.0, capText)
	captionBox.place(relx=0.5, rely=0.1, anchor="n", relheight = 0.23, relwidth = 0.4)

def makeCaps(numCaps, root):
	numTimes = 0
	nex = tk.StringVar()
	nex.set("Next")
	nextButton = tk.Button(root, font=("arial", 12), fg="#3d4849", bg="#e5e5e5", textvariable=nex, command=lambda:createCap(root))
	nextButton.place(relx=0.5, rely=0.4)
	for x in range(int(numCaps)):
		createCap(root)
		numTimes = numTimes + 1


def main():
	root = tk.Tk()
	root.geometry("700x900")
	root.title("IG Caption Maker")
	root.resizable(False, False)
	bgLabel = tk.Label(root, bg="#E5E5E5")
	bgLabel.place(relheight=1, relwidth=1)
	desText = tk.Label(root, fg="#3d4849", bg="#E5E5E5", font=("Arial", 16))
	desText["text"] = "How many captions do you need?"
	desText.place(relx=0.5, rely=0.03, anchor="n")
	entry = tk.Entry(root, borderwidth = 0, highlightthickness = 0, font=("Arial", 20), fg="#3d4849", justify="center")
	entry.place(relx=0.5, rely=0.1, anchor="n", relheight=0.06, relwidth=0.2)
	btnText = tk.StringVar()
	btnText.set("Go!")
	goButton = tk.Button(root, font =("arial bold", 10), fg= "#3d4849", bg="#e5e5e5", textvariable=btnText, command=lambda:[makeCaps(entry.get(), root), goButton.destroy(), desText.destroy(), entry.destroy()])
	goButton.place(relx=0.7, rely=0.115, anchor="n")
	root.mainloop()

if __name__ == '__main__':
	main()
