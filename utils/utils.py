def serialize_text_into_set(file: str):
    print(f"Tokenizing file {file}")
    f = open(file, "r")
    text = set(word.lower() for line in f for word in line.split() if word.isalpha())
    f.close()
    return text


def print_documents(corpus, file_names, ids):
    for id in ids:
        text = corpus.words(file_names[id])
        print('Document ID: '+str(id))
        for word in text:
            print(word,end=' ')
        print('\n')