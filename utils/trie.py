# transistion
    # [
        # state 0 -> {
        #     'a' --> { .. }
        #     'b' --> { .. }
        # }
    # ]

class Trie:
    def __init__(self):
        self.transitions = [{}] # init the 0 state that reads the empty string/epsilon
        self.final_states = set()

    def add_word(self, word: str):
        state, symbols_read = self.traverse(word)
        while symbols_read < len(word):
            new_state = len(self.transitions)
            self.transitions.append({})
            state = self.transitions[state]
            state[word[symbols_read]] = new_state
            state = new_state
            symbols_read += 1

    def traverse(self, word: str, initial_state = 0):
        state = initial_state
        symbols_read = 0

        while symbols_read < len(word) and word[symbols_read] in self.transitions[state]:
            state = self.transitions[state][word[symbols_read]]
            symbols_read += 1
        return state, symbols_read

    def isFinal(self, s):
        return s in self.final_states

    def is_in_trie(self, word: str):
        s, i = self.traverse(word)
        return i == len(word) and self.isFinal(s)

    def lst_words_with_prefix(self, prefix: str):
        s, i = self.traverse(prefix)
        return [ prefix + sufix for sufix in self.get_language_of_state(s)]

    def get_language_of_state(self, s):
        language = []
        if s in self.final_states:
            return language
        transitions_from_s = self.transitions[s]
        for (symbol, destination) in transitions_from_s.items():
            language += [ symbol + word for word in self.get_language_of_state(destination) ]
        return language

    def display(self):
        print("Transitions: ", self.transitions)
        print("Final states: ", self.final_states)
