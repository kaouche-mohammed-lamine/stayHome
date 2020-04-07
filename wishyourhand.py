from textblob import TextBlob
import csv

text = TextBlob("اغسلو ايديكم وابقو في منازلكم !!")
#print(text.detect_language())
print("( 0 )  "+text.string)
with open('LanguageCodeISO.csv', newline='') as f:
	reader = csv.reader(f)
	codeOld=""
	i=1
	for row in reader:
		code = row[0].split("-")
		codeOld = code[0]
		print("( "+str(i)+" )  "+" ( code = "+codeOld+" )  "+text.translate(to=codeOld).string)
		i=i+1
