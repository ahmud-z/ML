from textblob import TextBlob

text = input("Enter your text or review: ")

blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment >= 0:
    print("Positive Review")
else:
    print("Negative Review")
