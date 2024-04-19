import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("text", help="Input text, wrap it in quotes")
parser.add_argument(
    "-p", "--probability", metavar="P", type=int, default=15, help="Probability of a word to be quotified (an integer between 0 and 100, defaults to 15)")
parser.add_argument(
    "-n", "--amount", metavar="N", type=int, help="Exact amount of words to be quotified")

args = parser.parse_args()
if args.probability < 0 or args.probability > 100:
    raise ValueError(
        "Probability must be an integer between 0.0 and 1.0")

result = []
initial_text = args.text
initial_text = initial_text.strip()
initial_text = initial_text.split(" ")
text = []
for word in initial_text:
    if word:
        text.append(word)

if args.amount:
    if args.amount > len(text):
        args.amount = len(text)
    chosen_words = random.sample(text, args.amount)
    for word in text:
        if word in chosen_words:
            new_word = f"\"{word}\""
            chosen_words.remove(word)
        else:
            new_word = word
        result.append(new_word)
    result = " ".join(result)
else:
    for word in text:
        ticket = random.randint(0, 100)
        if ticket < args.probability:
            result.append(f"\"{word}\"")
        else:
            result.append(word)
    result = " ".join(result)

print(result)
