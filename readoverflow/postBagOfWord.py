import sys
from bs4 import BeautifulSoup
import re
import numpy as np


# Common Vectorizer doesn't work very well since we have too many words
# https://scikit-learn.org/stable/modules/feature_extraction.html#the-bag-of-words-representation
#
# from sklearn.feature_extraction.text import CountVectorizer
# import numpy as np
# vectorizer = CountVectorizer()

# Trying sparse vectorizer
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html
#
from sklearn.feature_extraction.text import HashingVectorizer
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# from gensim.models.doc2vec import TaggedDocument, Doc2Vec

# I could use pandas but here it's very simple.


# def get_stop_words(stop_words_file):
#     stop_words = []
#     with open(stop_words_file, "rt") as swf:
#         for line in swf:
#             words = line.split()
#             for word in words:
#                 stop_words.append(word)
#     return stop_words


def clean_text(text):
    global EMPTY
    EMPTY = ''

    if not isinstance(text, str):
        return text
    text = re.sub('<pre><code>.*?</code></pre>', EMPTY, text)

    def replace_link(match):
        return EMPTY if re.match('[a-z]+://', match.group(1)) else match.group(1)

    text = re.sub('<a[^>]+>(.*)</a>', replace_link, text)
    return re.sub('<[^>]+>', EMPTY, text)


def main(argv):
    # stop_words = get_stop_words('stopwords.txt')
    vectorizer = HashingVectorizer(stop_words='english', alternate_sign=False, n_features=2**5)
    # tfidf  = TfidfVectorizer()

    count = 0
    corpus = []
    js = np.arange(654)
    with open(argv[1], "rt") as csvf:
        for line in csvf:
            cols = line.split(",")
            soup = BeautifulSoup(cols[2], 'html.parser')
            cleaned_text = clean_text(soup.get_text())
            cleaned_text = cleaned_text.replace("?", "")
            cleaned_text = cleaned_text.replace("_", "")
            cleaned_text = cleaned_text.replace("#", "")
            cleaned_text = cleaned_text.replace(";", "")
            cleaned_text = cleaned_text.replace("/", " ")
            cleaned_text = cleaned_text.replace("*", " ")
            cleaned_text = cleaned_text.replace("+", " ")
            cleaned_text = cleaned_text.replace("\\", " ")
            cleaned_text = cleaned_text.replace("^", " ")
            cleaned_text = cleaned_text.replace("%", " ")
            cleaned_text = cleaned_text.replace("|", " ")
            cleaned_text = cleaned_text.replace(">", " ")
            cleaned_text = cleaned_text.replace("'", " ")
            cleaned_text = cleaned_text.replace(">", " ")
            cleaned_text = cleaned_text.replace("<", " ")
            cleaned_text = cleaned_text.replace("-", " ")
            cleaned_text = cleaned_text.replace(":", " ")
            cleaned_text = cleaned_text.replace("[", " ")
            cleaned_text = cleaned_text.replace("]", " ")
            cleaned_text = cleaned_text.replace("{", " ")
            cleaned_text = cleaned_text.replace("}", " ")
            cleaned_text = cleaned_text.replace("(", " ")
            cleaned_text = cleaned_text.replace(")", " ")
            cleaned_text = cleaned_text.replace("=", " ")
            cleaned_text = cleaned_text.replace(".", " ")
            cleaned_text = cleaned_text.replace("!", " ")
            cleaned_text = cleaned_text.replace("0", " ")
            cleaned_text = cleaned_text.replace("1", " ")
            cleaned_text = cleaned_text.replace("2", " ")
            cleaned_text = cleaned_text.replace("3", " ")
            cleaned_text = cleaned_text.replace("4", " ")
            cleaned_text = cleaned_text.replace("5", " ")
            cleaned_text = cleaned_text.replace("6", " ")
            cleaned_text = cleaned_text.replace("7", " ")
            cleaned_text = cleaned_text.replace("8", " ")
            cleaned_text = cleaned_text.replace("9", " ")
            cleaned_text = cleaned_text.lower()
            cleaned_text = cleaned_text.lower()
            corpus.append(cleaned_text)
            # print(corpus[-1])
            # print(cols[18].lower().find("javascript"))
            js[count] = (cols[18].lower().find("javascript") >= 0)
            if count == 653:
                break
            # print(f"count = {count}")
            count += 1

    x = vectorizer.fit_transform(corpus).toarray()
    # x =  tfidf.fit_transform(corpus).toarray()
    # x = Doc2Vec(corpus, size=5, min_count=0).docvecs
    # print(f"x.shape = {x.shape}, js.shape = {js.shape}")
    r = np.hstack((x, js.reshape(654, 1)))
    np.savetxt("vector.csv", r, delimiter=",", newline='\n')
    # np.savetxt("tfidf.csv", r, delimiter=",", newline='\n')


if __name__ == "__main__":
    main(sys.argv)
