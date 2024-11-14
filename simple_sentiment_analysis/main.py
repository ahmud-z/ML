from textblob import TextBlob

text = input("Enter your text or review: ")

blob = TextBlob(text)
sentiment = blob.sentiment.polarity

print(f"Score: {sentiment}")

if sentiment > 0:
    print("positive")
elif sentiment < 0:
    print("negative")
else:
    print("neutral")

