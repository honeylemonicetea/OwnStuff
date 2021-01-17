from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


final_words=[]
raw_sent = "i saw the sky it was falling on me so fast i was scared and terrified and sad"
raw_sent = word_tokenize(raw_sent, "english")
for word in raw_sent:
    if word not in stopwords.words("english"):
        final_words.append(word)
emotion_list = []
with open("emotions.txt", "r") as file:
    for line in file:
        clear_line = line.replace("\n", "").replace(",","").replace("'","").strip()
        word, emotion = clear_line.split(": ")
        if word in final_words:
            emotion_list.append(emotion)
# print(emotion_list)
w = Counter(emotion_list)
# print(w)

def sentimemnt_analyse(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)

    print(score)

sentimemnt_analyse(raw_sent)

plt.bar(w.keys(),w.values())
plt.savefig("graph.png")
plt.show()