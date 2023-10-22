import math
from .utils import tokenize_file

def train_bernoulli(train_corpus):
    N =  sum(len(class_lst) for class_lst in train_corpus)
    class_cnt = len(train_corpus)
    V = {}
    i = 0
    for c in range(class_cnt):
        for file in train_corpus[c]:
            i += 1
            terms = tokenize_file(file)
            for term in terms:
                if term not in V:
                    V[term] = [0] * class_cnt
                V[term][c] += 1
    Nc = [ len(class_lst) for class_lst in train_corpus ]
    prior_probability = [ Nc[c] / N for c in range(class_cnt) ]
    cond_probability = {}
    for term in V:
        cond_probability[term] = [(V[term][class_index] + 1 ) / (Nc[class_index] + 2 ) for class_index in range(class_cnt)]
    return cond_probability, prior_probability, V

def calculate_initial_cond_probability(cond_probability, features = None):
    class_cnt = len(cond_probability)
    initial_cond_probability = [0.0] * class_cnt
    for term in features if features else cond_probability:
        for c in range(class_cnt):
            initial_cond_probability[c] += math.log(1.0 - cond_probability[term][c])
    return initial_cond_probability

def apply_bernoulli(prior_probability, conditional_probability, initial_cond_probability, text, features = None ):
    terms = tokenize_file(text)
    classes_cnt = len(prior_probability)
    for c in range(classes_cnt):
        score = math.log(prior_probability[c]) + initial_cond_probability[c]
        for term in terms:
            if term not in conditional_probability: continue
            if features and term not in features: continue
            score += math.log( conditional_probability[term][c] / (1.0 - conditional_probability[term][c]))
        if c == 0 or score > max_score:
            max_score = score
            answer = c
    return answer