from textblob import TextBlob


class ReportDetails:
    def __init__(self, tweets: list):
        """
        Usage:
        report = ReportDetails(tweets)


        """
        self.tweets = tweets
        self.words = self.get_words_from_tweets()

    # def get_avg_positivity_score(self) -> int:
    #     avg_positivity_score = 0
    #     tweets_scores = []
    #     for tweet in self.tweets:
    #         score = TextBlob(tweet.text).sentiment.polarity
    #         score = score * 100
    #         tweets_scores.append(score)
    #     avg_positivity_score = int(sum(tweets_scores) / len(tweets_scores))
    #     return avg_positivity_score

    @staticmethod
    def get_positivity_score(words: list):
        scores = []
        for word in words:
            score = TextBlob(word).sentiment.polarity
            scores.append(score)
        return scores

    def get_words_from_tweets(self):
        words = []
        for tweet in self.tweets:
            blob = TextBlob(tweet.text)
            words.extend(blob.tags)
        return words

    def get_most_used_words(self, pos: list):
        """
        Usage:
        After passing tweets to get_words_from_tweets(), call this method along with tag
        name to get a list of the words and how many times it was used

        Additional Info:
        Refer to https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html for pos tags.
        """
        words = []
        for word in self.words:
            if word[1] in pos and word[0].isalnum():
                words.append((word[0], word[1], self.words.count(word)))
                if len(words) == 10:
                    break
        sorted_list = set(sorted(words, key=lambda tup: tup[2], reverse=True))
        # print("#######")
        # print(sorted_list)
        return [word[0] for word in sorted_list], [word[2] for word in sorted_list]
