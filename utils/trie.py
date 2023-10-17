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
    
    def display(self):
        print("Transitions: ", self.transitions)
        print("Final states: ", self.final_states)
