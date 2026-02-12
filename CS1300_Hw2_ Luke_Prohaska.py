CURRENT_YEAR = 2026
BORDER = "=" * 30

first_name = input("Luke:")
last_name = input("Prohaska:")

birth_year = int(input("2006:"))
hobby = input("Fishing:")

first_name = first_name.title()
last_name = last_name.title()

age = CURRENT_YEAR - birth_year

print(f"\n{BORDER}")
print(f"{'USER PROFILE CARD':^30}")
print(f"{BORDER}")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print(f"{'Thank you for creating your profile!':^30}")
print(f"{BORDER}")





sentence = input("I love to go fising on the weekend with my dad:")

total_chars = len(sentence)
total_no_spaces = len(sentence.replace("", ""))
word_count = len(sentence.split())

vowels = "aeiou"
vowel_count = sum(1 for char in sentence.lower() if char in vowels)

uppercase = sentence.upper()
lowercase = sentence.lower()
reversed_sentence = sentence[::-1]

starts_with_capital ="Yes" if sentence[0].isupper() else "No"
ends_with_punct = "Yes" if sentence.endswith(('.', '!', '?'))else "No"

print("\n=== TEXT ANALYZER ===")
print(f"Total characters (with spaces): {total_chars}")
print(f"Total characters (without spaces): {total_no_spaces}")
print(f"Number of words: {word_count}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase version: {uppercase}")
print(f"Lowercase version: {lowercase}")
print(f"Reversed: {reversed_sentence}")
print(f"Starts with capital: { starts_with_capital}")
print(f"Ends with punctuation: {ends_with_punct}")






