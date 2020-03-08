from textblob import TextBlob


class ReportDetails:
    def __init__(self, tweets: list):
        self.tweets = tweets
        self.words = self.get_words_from_tweets()

    def get_avg_positivity_score(self) -> int:
        avg_positivity_score = 0
        tweets_scores = []
        for tweet in self.tweets:
            score = TextBlob(tweet.text).sentiment.polarity
            score = score * 100
            tweets_scores.append(score)
        avg_positivity_score = int(sum(tweets_scores) / len(tweets_scores))
        return avg_positivity_score

    def get_words_from_tweets(self):
        words = []
        for tweet in self.tweets:
            blob = TextBlob(tweet.text)
            words.extend(blob.tags)
        return words

    def get_most_used_words(self, word_part) -> str:
        words = []
        for word in self.words:
            if word[1] == word_part and word[0].isalnum():
                words.append((word[0], word[1], self.words.count(word)))
        sorted_list = set(sorted(words, key=lambda tup: tup[2], reverse=True)[0:1])
        return ", ".join([word[0] for word in sorted_list])
