def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def count_sentences(text):
    sentences = text.split(".")
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def count_paragraphs(text):
    paragraphs = text.split("\n\n")
    paragraphs = [p for p in paragraphs if p.strip()]
    return len(paragraphs)

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def longest_sentences(text):
    sentences = text.split(".")
    sentences = [s for s in sentences if s.strip()]
    if not sentences:
        return ""
    return max(sentences, key=len)

def longest_paragraph(text):
    paragraphs = text.split("\n\n")
    paragraphs = [p for p in paragraphs if p.strip()]
    if not paragraphs:
        return ""
    return max(paragraphs, key=len)

def test_count_words():
    text = "Hola mundo"
    assert count_words(text) == 2

def test_count_characters():
    text = "Hola"
    assert count_characters(text) == 4

def test_count_sentences():
    text = "Hola mundo. Esto es una prueba"
    assert count_sentences(text) == 2

def test_longest_word():
    text = "Hola mundo de programacion"
    assert longest_word(text) == "programacion"

if __name__ == '__main__':
    print("Ejecutando tests....")
    test_count_words()
    test_count_characters()
    test_count_sentences()
    test_longest_word()
    print("Todos los test pasaron")
