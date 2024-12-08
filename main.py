def count_words(words):
    num = len(words.split())
    return(num)

def count_chars(text):
    lowered_text =text.lower()
    letter_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
        }
    for char in lowered_text:
        if char in letter_count:
            letter_count[char] += 1
    return(letter_count)
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    total = count_words(file_contents)
    per_letter = count_chars(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---\n {total} words found in the document")
    for letter in per_letter:
        num_of_times = per_letter[letter]
        print(f"the {letter} character was found {num_of_times} times")
main()
