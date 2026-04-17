import random
import string
import time

# الكلمات الأساسية
names = ["Ali1990"]
cars = ["Nissan_Ahmed"]
teams = ["Messi@1990"]
apps = ["Siri2024!"]

words = names + cars + teams + apps

specials = ["@", "#", "_", "!", "$"]

passwords = set()

start = time.time()

# دوال لتوليد أنماط مختلفة
def pattern1():
    return random.choice(words) + str(random.randint(0, 9999))

def pattern2():
    return random.choice(words) + random.choice(specials) + str(random.randint(0, 9999))

def pattern3():
    return str(random.randint(0, 9999)) + random.choice(words)

def pattern4():
    word = random.choice(words)
    return word.upper() + random.choice(specials) + str(random.randint(0, 9999))

def pattern5():
    word = random.choice(words)
    mixed = ''.join(random.choice([c.upper(), c.lower()]) for c in word)
    return mixed + random.choice(specials) + str(random.randint(0, 9999))

patterns = [pattern1, pattern2, pattern3, pattern4, pattern5]

# توليد 100000 كلمة سر بدون تكرار
while len(passwords) < 100000:
    pwd = random.choice(patterns)()
    passwords.add(pwd)

# حفظ في ملف
with open("passwords.txt", "w") as file:
    for password in passwords:
        file.write(password + "\n")

end = time.time()

print("✅ Successfully generated 100000 passwords")
print("📁 Saved to: passwords.txt")
print(f"⏱ Time elapsed: {end - start:.2f} seconds")
