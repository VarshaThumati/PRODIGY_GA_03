import markovify
from pathlib import Path


# Get the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
CORPUS_PATH = BASE_DIR / "data" / "corpus.txt"
OUTPUT_PATH = BASE_DIR / "outputs" / "generated_text.txt"

# Create outputs folder
OUTPUT_PATH.parent.mkdir(exist_ok=True)


# Load the training corpus
with open(CORPUS_PATH, "r", encoding="utf-8") as file:
    text = file.read()


# Build the Markov Chain model
model = markovify.Text(text, state_size=2)


print("=" * 65)
print("       PRODIGY TASK 03 - MARKOV CHAIN TEXT GENERATOR")
print("=" * 65)

print("\nTraining corpus loaded successfully.")
print(f"Corpus size: {len(text)} characters")

print("\nThe model has learned word relationships from the corpus.")
print("You can now provide a starting word or phrase.")

# Get user input
start = input("\nEnter a starting word or phrase: ").strip()

if start and start.lower() not in text.lower():
    print("\nStarting word/phrase not found in the corpus.")
    print("Please try a word such as:")
    print("artificial, machine, Python, text, Markov, learning, data")
    exit()


# Generate text
generated_text = []

print("\nGenerating text...\n")

for i in range(5):

    if start:
        sentence = model.make_sentence_with_start(
            beginning=start,
            strict=False,
            tries=100
        )
    else:
        sentence = model.make_sentence(tries=100)

    if sentence:
        generated_text.append(sentence)
        print(f"{i + 1}. {sentence}")
    else:
        print(f"{i + 1}. Unable to generate text.")


# Save generated text
with open(OUTPUT_PATH, "w", encoding="utf-8") as file:

    file.write("PRODIGY TASK 03 - MARKOV CHAIN TEXT GENERATION\n")
    file.write("=" * 55 + "\n\n")

    file.write(f"Starting phrase: {start}\n\n")

    for i, sentence in enumerate(generated_text, start=1):
        file.write(f"{i}. {sentence}\n")


print("\n" + "=" * 65)
print(f"Generated text saved to:")
print(OUTPUT_PATH)
print("=" * 65)