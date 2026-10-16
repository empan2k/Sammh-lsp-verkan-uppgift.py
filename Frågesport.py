points = 0

# Fråga 1
print("-" * 71)
print("1. Vem är den första programeraren?")
print("""A. Charles Babbage
B. Alan Turing
C. Ada Lovelace
D. Grace Hopper""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "C":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 2
print("-" * 71)
print("2. Vem utvecklade det moderna programmeringsspråket COBOL?")
print("""A. Grace Hopper
B. Ada Lovelace
C. Margaret Hamilton
D. Charles Babbage""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 3
print("-" * 71)
print("3. Under vilket årtal levde Ada Lovelace?")
print("""A. 1600-talet
B. 1700-talet
C. 1800-talet
D. 1900-talet""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "C":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 4
print("-" * 71)
print("4. När introducerades hålkort för tidigare datorer?")
print("""A. 1500-talet
B. 1900-talet
C. 1500-talet
D. 2000-talet""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "B":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 5
print("När blev CSS, HTML och JavaScript viktiga?")
print("""A. 1900-talet
B. 1950-talet
C. 1990-talet
D. 2000-talet""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "C":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 6
print("När blev webbsidor snygga och interaktiva?")
print("""A. 1700-talet
B. 1800-talet
C. 1990-talet
D. 2000-talet""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "C":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 7
print("När gjorde hålkort sin entré inom programmering?")
print("""A. 1700-talet
B. 1800-talet
C. 2000-talet
D. 1900-talet""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "D":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 8
print("Vad använde man hålkort till?")
print("""A. Att skicka sms.
B. Att programmera de tidiga datorerna.
C. Att skriva brev.
D. Att skriva böcker.""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "B":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 9
print("Vad hette den tidiga datorn som användes för komplicerade beräkningar under andra världskriget?")
print("""A. ENIAC
B. Android
C. Apple
D. Microsoft""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "A":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)

# Fråga 10
print("Vilka appar nämns i texten?")
print("""A. Snapchat
B. TikTok
C. Spotify
D. WhatsApp""")

while True:
    answer = input("svar: ")
    if answer:
        break

if answer.upper() == "C":
    print("Rätt!")
    points += 1
else:
    print("Fel!")
    points -= 1

print("Total poäng: ", points)
print("Tack för att du körde min frågesport!")