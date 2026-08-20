import random
import string

message = input("Enter the messege-: ")

words = message.split()
result = []

for word in words:
    if len(word) >= 3:
        new_word = word[1:] + word[0]

        random_start = ''.join(random.choices(string.ascii_letters, k = 3))
        random_end = ''.join(random.choices(string.ascii_letters, k = 3))

        new_word = random_start + new_word + random_end

        result.append(new_word)

    else:
        result.append(word[::-1])

print ("secret message: ", " ".join(result))