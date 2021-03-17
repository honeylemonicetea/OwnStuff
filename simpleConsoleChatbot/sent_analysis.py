# import nltk

# words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]


# stop_ws = nltk.corpus.stopwords.words('english')
# words = [w for w in words if w.lower() not in stop_ws]

# text = 'No, really, you’re amazing. I can’t stand that sort of guy. He just rubs me the wrong way. But you, well, sometimes you join in when me and Mrs. Izumi are wound up about something, but you yourself never complain, do you? I’ve never seen you get upset even with an annoying newbie.'
#
# print(nltk.word_tokenize(text))
# tokens = nltk.word_tokenize(text)
# tokens = [w for w in tokens if w.isalpha() and w.lower() not in stop_ws]
# print(tokens)
# words: list[str] = tokens
# fd = nltk.FreqDist(words)
# fd.most_common(3)
# fd.tabulate(3)
# text = nltk.Text(tokens)
# fd = text.vocab()
# fd.tabulate(4)
#
# finder = nltk.collocations.TrigramCollocationFinder.from_words(words)
# finder.ngram_fd.tabulate(3)

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from random import shuffle
from statistics import mean

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("i've had a really really bad day and eveything was awful"))

# tweets = [t.replace('://','//') for t in nltk.corpus.twitter_samples.strings()]
positive_review_ids = nltk.corpus.movie_reviews.fileids(categories = ['pos'])
negative_review_ids = nltk.corpus.movie_reviews.fileids(categories = ['neg'])
all_review_ids = positive_review_ids + negative_review_ids
#
# def is_positive(tweet:str) -> bool:
#     return sia.polarity_scores(tweet)['compound'] > 0

def is_pos(review_id: str) -> bool:
    text = nltk.corpus.movie_reviews.raw(review_id)
    scores = [
        sia.polarity_scores(sentence)['compound']
        for sentence in nltk.sent_tokenize(text)
    ]
    return mean(scores) > 0

# shuffle(tweets)
#
# for tweet in tweets[:10]:
#     print('>',is_positive(tweet), tweet)

# shuffle(all_review_ids)
# correct = 0
# for review_id in all_review_ids:
#     if is_pos(review_id):
#         if review_id in positive_review_ids:
#             correct += 1
#     else:
#         if review_id in negative_review_ids:
#             correct += 1
#
# print(f'{correct/len(all_review_ids): .2%} correct')
# unwanted = nltk.corpus.stopwords.words('english')
# unwanted.extend([w.lower() for w in nltk.corpus.names.words()])
#
# def skip_unwanted(pos_tuple):
#     word, tag = pos_tuple
#     if not word.isalpha() or word in unwanted:
#         return False
#     if tag.startswith('NN'):
#         return False
#
# positive_words = [word for word, tag in  filter(skip_unwanted, nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=['pos' ]))                                                )]
# negative_words = [word for word, tag in  filter(skip_unwanted, nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=['neg' ]))                                                )]
# print(positive_words)
# print(negative_words)
#
# unwanted = nltk.corpus.stopwords.words("english")
# unwanted.extend([w.lower() for w in nltk.corpus.names.words()])
#
# def skip_unwanted(pos_tuple):
#     word, tag = pos_tuple
#     if not word.isalpha() or word in unwanted:
#         return False
#     if tag.startswith("NN"):
#         return False
#     return True
#
# positive_words = [word for word, tag in filter(
#     skip_unwanted,
#     nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["pos"]))
# )]
# negative_words = [word for word, tag in filter(
#     skip_unwanted,
#     nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["neg"]))
# )]
# print(positive_words[:100])