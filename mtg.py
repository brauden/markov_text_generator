import nltk
import numpy as np
from collections import Counter


def make_ngram(token, n, pred=False):
    ngrams = zip(*[token[i:] for i in range(n)])
    ngrams = list(ngrams)
    if pred:
        ngrams = [x[1:] for x in ngrams]
        return ngrams
    return ngrams


def count_frequency(ngram, n):
    counter = Counter(ngram)
    counter = counter.most_common(len(counter))
    if len(ngram[0]) >= 2:
        norm = sum(x[1] for x in counter)
        counter = [list(x) for x in counter]
        norm_counter = [[x[0], x[1] / norm] for x in counter]
        if len(ngram[0]) == 2:
            norm_counter = [((x[0][0],), x[0][1], x[1]) for x in norm_counter]
        else:
            norm_counter = [(x[0][:n - 1], x[0][n - 1], x[1]) for x in norm_counter]
        return norm_counter
    elif len(ngram[0]) == 1:
        norm = sum(x[1] for x in counter)
        return [[x[0], x[1] / norm] for x in counter]


def finish_sentence(sentence, n, corpus, deterministic=False):
    result = []
    result += sentence
    max_len = 15
    stop_chars = ['.', '?', '!']
    ngram_corpus = make_ngram(corpus, n)
    distribution = count_frequency(ngram_corpus, n)
    while result[-1] not in stop_chars and len(result) < max_len:
        ngram_sentence = make_ngram(result, n, True)
        filtered = []
        for ngram in distribution:
            if ngram[0] == ngram_sentence[-1]:
                filtered.append(list(ngram[1:]))
        if len(filtered) == 0:
            for i in range(1, n):
                i_ngram_c = make_ngram(corpus, n - i)
                i_dist = count_frequency(i_ngram_c, n - 1)
                i_ngram_s = make_ngram(result, n - i, True)
                for igram in i_dist:
                    if igram[0] == i_ngram_s[-1]:
                        filtered.append(list(igram[1:]))
                if len(filtered) > 0:
                    break
            if len(filtered) == 0:
                d = count_frequency(corpus, 1)
                filtered.append(np.random.choice([x[0] for x in d], p=[x[1] for x in d]))
        if deterministic:
            result.append(max(filtered, key=lambda x: x[1])[0])
        else:
            weights = [d[1] for d in filtered]
            weights = [d / sum(weights) for d in weights]
            choice = np.random.choice([d[0] for d in filtered], p=weights)
            result.append(choice)
    return result


if __name__ == '__main__':
    corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
    corpus = nltk.word_tokenize(corpus.lower())
    s1 = ['it', 'is', 'very', 'generous']
    s2 = ['there', 'are', 'several']
    s3 = ['it', 'sdafs', 'nice']
    print(finish_sentence(s2, 2, corpus, True))
    print(finish_sentence(['she', 'was', 'not'], 3, corpus, False))
    print(finish_sentence(s1, 4, corpus, False))
    print(finish_sentence(s3, 3, corpus, False))
