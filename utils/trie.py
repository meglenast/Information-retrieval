class Trie:
    def __init__(self):
        self.transitions = [{}]
        self,final_states = set()

    def add_word(self, word: str):
        state, number_chars_read = self.traverse(word)
        while number_chars_read < len(word):
            new_state = len(self.transitions)
            self.transitions.append({})
            state = self.transitions[s]
            state[word[i]] = new_state
            state = new_state
            number_chars_read += 1

    def __traverse__(self, word: str, initial_state = 0):
        state = initial_state
        number_chars _read = 0

        while number_chars_read < len(word) and word[number_chars_read] in self.transitions[state]:
            state = self.transitions[state][word[number_chars_read]]
            number_chars_read += 1
        return state, number_chars_read
