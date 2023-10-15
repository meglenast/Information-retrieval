class Tokenizer:

    def __init__(self, files):

    def serialize_files_into_set(files: list[str]):
        dictionary = {}
        for file in files:
            print(f"Serailizing file {file}...")
            dictionary.in

    def serialize_text_into_set(file: str):
        f = open(file, "r")
        text = set(word.lower() for line in f for word in line.split() if word.isalpha())
        f.close()
        return text
