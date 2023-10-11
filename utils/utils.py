def serialize_text_into_array(file: str):
    f = open(file, "r")
    text =[word for line in f for word in line.split()]
    f.close()
    return text

