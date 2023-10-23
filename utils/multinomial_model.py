import math
from .utils import tokenize_file

def train_multinomial(train_corpus):
    N = sum(len(class_lst) for class_lst in train_corpus)
    class_cnt = len(train_corpus)
    V = {}
    i = 0
    for c in range(class_cnt):
        for text in train_corpus[c]:
            terms = tokenize_file(text)
            for term in terms:
                if term not in v:
                    V[term] = [0] * class_cnt
                V[term][c] += 1

    Nc = [ len(class_lst) for class_lst in train_corpus ]
    prior_probability = [ Nc[c] / N for c in range(class_cnt) ]
    T = [0] * class_cnt
    for term in V:
        for c in range(class_cnt):
            T[c] += V[t][c]
    cond_probability = {}
    for t in V:
        cond_probability[t] = [ (V[t][c] + 1) / (T[c] + len(V)) for c in range(class_cnt)]
    return cond_probability, prior_probability, V


def apply_multinomial(prior, conditional_probability, text, features = None):
    terms = tokenize_file(text)
    class_cnt = len(prior)
    for c in range(class_cnt):
        score = math.log(prior[c])
        for term in terms:
            if t not in conditional_probability: continue
            if features and term not in features: continue
            score += math.log(conditional_probablity[term][c])
        if c == 0 or score > maxScore:
            maxScore = score
            answer = c
    return answer
