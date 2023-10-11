from .utils import serialize_text_into_array

class ReverseIndex:
    def __init__(self, files):
        self.r_idex = self.build_r_index(files)

    def build_r_index(self, files):
        ri = {}
        for idx, file in enumerate(files):
            words = serialize_text_into_array(file)

            for word in words:
                if word not in ri:
                    ri[word] = [idx]
                else:
                    (ri[word]).append(idx)

        print(ri)