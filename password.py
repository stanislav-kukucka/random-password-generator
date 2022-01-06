import secrets
import random, string

line = "-" * 40
password_length = 30
symbols = string.punctuation
char = symbols + secrets.token_urlsafe()
rnd = random.SystemRandom()

print (line)
print("".join(rnd.choice(char) for i in range(password_length)))
print (line)
