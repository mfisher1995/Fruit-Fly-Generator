# Simplified Genotype Generator
from cs50 import get_string

# Allele frequencies for mutations

wings = {}

Cy = 0.50
WTw = 0.50

wings['curly'] = Cy
wings['WTwing'] = WTw

eyes = {}

w = 0.25
WTe = 0.75

eyes['white'] = w
eyes['WTeye'] = WTe

body = {}

e = 0.25
WTb = 0.75

body['ebony'] = e
body['WTbody'] = WTb

# Print description of this tool

print("----Welcome to the Fruit Fly Generator!----\n"\
"This application is a fly cross prediction simulator. Enter the phenotypes for each\n"\
"parent fly and the application will reveal your progeny's genotype and phenotype\n"\
"breakdown as percentages. This application is a simplified tool for how to predict \n"\
"crosses in real life using the Hardy-Weinberg Model: \n"
"\n(p^2)+2(p*q)+(q^2) = 1\n"\
"\nThis model inputs allelic frequencies (p and q) and determines the result genotype \n"\
"and phenotype frequencies of the progeny population according to Mendelian Laws of \n" \
"dominant vs recessive genes.\n"\
"Are you ready to see the possible phenotypes?")

ready = get_string("Y/N? \n")
print("\n")
if ready == 'Y':
    print("The following mutations are available to use:\n"\

    "Wings:\n"\
    "   1. curly (Cy)\n"\
    "   2. WTwing (WT)\n"\
    "Eye Color\n"\
    "   1. white (w)\n"\
    "   2. WTeye (WT)\n"\
    "Body Color\n"\
    "   1. ebony (e)\n"\
    "   2. WTbody (WT)\n"\
    "\n"\
    "***PLEASE NOTE***\n"\
    "When choosing the phenotype for your parent flies, it is crucial to type them\n"\
    "exactly as written: curly, WTwing, white, WTeye, ebony, WTbody. WT Stands for WildType.")
elif ready == 'Yes':
    print("The following mutations are available to use:\n"\

    "Wings:\n"\
    "   1. curly (Cy)\n"\
    "   2. WTwing (WT)\n"\
    "Eye Color\n"\
    "   1. white (w)\n"\
    "   2. WTeye (WT)\n"\
    "Body Color\n"\
    "   1. ebony (e)\n"\
    "   2. WTbody (WT)\n"\
    "\n"\
    "***PLEASE NOTE***\n"\
    "When choosing the phenotype for your parent flies, it is crucial to type them\n"\
    "exactly as written: curly, WTwing, white, WTeye, ebony, WTbody. WT Stands for WildType")
elif ready == 'y':
    print("The following mutations are available to use:\n"\

    "Wings:\n"\
    "   1. curly (Cy)\n"\
    "   2. WTwing (WT)\n"\
    "Eye Color\n"\
    "   1. white (w)\n"\
    "   2. WTeye (WT)\n"\
    "Body Color\n"\
    "   1. ebony (e)\n"\
    "   2. WTbody (WT)\n"\
    "\n"\
    "***PLEASE NOTE***\n"\
    "When choosing the phenotype for your parent flies, it is crucial to type them\n"\
    "exactly as written: curly, WTwing, white, WTeye, ebony, WTbody. WT Stands for WildType")
elif ready == 'yes':
    print("The following mutations are available to use:\n"\

    "Wings:\n"\
    "   1. curly (Cy)\n"\
    "   2. WTwing (WT)\n"\
    "Eye Color\n"\
    "   1. white (w)\n"\
    "   2. WTeye (WT)\n"\
    "Body Color\n"\
    "   1. ebony (e)\n"\
    "   2. WTbody (WT)\n"\
    "\n"\
    "***PLEASE NOTE***\n"\
    "When choosing the phenotype for your parent flies, it is crucial to type them\n"\
    "exactly as written: curly, WTwing, white, WTeye, ebony, WTbody. WT Stands for WildType")
else:
    print("Sad to see you leave! To see phenotypes, restart. If you meant to say yes, please restart and type yes.")
    quit()

# Ask user to input Fly Parent 1 phenotypes: wings, eye color, body color
print("\n----Fly Parent 1:----")

# Prompt user for wing:
w1 = get_string("Fly Parent 1 Wing: ")
if w1 == 'curly':
    print("Great!")
elif w1 == 'WTwing':
    print("Great!")
else:
    print("Error please type in a valid WING phenotype")
    # Reprompt user for phenotype
    w1 = get_string("Fly Parent 1 Wing: ")
    if w1 == 'curly':
        print("Great!")
    elif w1 == 'WTwing':
        print("Great!")
    else:
        print("Did not follow directions. Start over.")
        quit()

# Prompt user for eye color:
e1 = get_string("Fly Parent 1 Eye Color: ")
if e1 == 'white':
    print("Great!")
elif e1 == 'WTeye':
    print("Great!")
else:
    print("Error please type in a valid EYE COLOR phenotype")
    # Reprompt user for phenotype
    e1 = get_string("Fly Parent 1 Eye Color: ")
    if e1 == 'white':
        print("Great!")
    elif e1 == 'WTeye':
        print("Great!")
    else:
        print("Did not follow directions. Start over.")
        quit()

# Prompt user for body color
b1 = get_string("Fly Parent 1 Body Color: ")
if b1 == 'ebony':
    print("Great!")
elif b1 == 'WTbody':
    print("Great!")
else:
    print("Error please type in a valid BODY COLOR phenotype")
    # Reprompt user for phenotype
    b1 = get_string("Fly Parent 1 Body Color: ")
    if b1 == 'ebony':
        print("Great!")
    elif b1 == 'WTbody':
        print("Great!")
    else:
        print("Did not follow directions. Start over.")
        quit()

# Ask user to input Fly Parent 2 phenotypes: wings, eye color, body color
print("\n----Fly Parent 2:----")

# Prompt user for wing:
w2 = get_string("Fly Parent 2 Wing: ")
if w2 == 'curly':
    print("Great!")
elif w2 == 'WTwing':
    print("Great!")
else:
    print("Error please type in a valid WING phenotype")
    # Reprompt user for phenotype
    w2 = get_string("Fly Parent 2 Wing: ")
    if w2 == 'curly':
        print("Great!")
    elif w2 == 'WTwing':
        print("Great!")
    else:
        print("Did not follow directions. Start over.")
        quit()

# Prompt user for eye color:
e2 = get_string("Fly Parent 2 Eye Color: ")
if e2 == 'white':
    print("Great!")
elif e2 == 'WTeye':
    print("Great!")
else:
    print("Error please type in a valid EYE COLOR phenotype")
    # Reprompt user for phenotype
    e2 = get_string("Fly Parent 1 Eye Color: ")
    if e2 == 'white':
        print("Great!")
    elif e2 == 'WTeye':
        print("Great!")
    else:
        print("Did not follow directions. Start over.")
        quit()

# Prompt user for body color
b2 = get_string("Fly Parent 2 Body Color: ")
if b2 == 'ebony':
    print("Great!")
elif b2 == 'WTbody':
    print("Great!")
else:
    print("Error please type in a valid BODY COLOR phenotype")
    # Reprompt user for phenotype
    b2 = get_string("Fly Parent 1 Body Color: ")
    if b2 == 'ebony':
        print("Great!")
    elif b2 == 'WTbody':
        print("Great!")
    else:
        print("Did not follow directions. Start over.")
        quit()

# Wings: Calculate Genotypes
x1 = ((wings[w1])**2) * 100
x2 = (2 * ((wings[w1] * wings[w2]))) * 100
x3 = ((wings[w2])**2) * 100

# Print pecerntage of phenotypes and genotypes for progeny flies
print("\nSuccess! Your progeny flies are listed below. Thank you for using\n"\
    "the Fruit Fly Generator!")
print("\n----PROGENY----")
print("WINGS")
if w1 == "curly" and w2 == "WTwing":
    print("Progeny Genotypes:", x1, "% Cy/Cy,", x2, "% WT/Cy,", x3, "% WT/WT")
    print("Progeny Phenotypes:", x1, "% Curly Wings,", (x2 + x3), "% WildType Wings")
elif w1 == "curly" and w2 == "curly":
    print("Progeny Genotypes: 100 % Cy/Cy")
    print("Progeny Phenotypes: 100 % Curly Wings")
elif w1 == "WTwing" and w2 == "curly":
    print("Progeny Genotypes:", x1, "% WT/WT,", x2, "% WT/Cy,", x3, "% Cy/Cy")
    print("Progeny Phenotypes:", (x1 + x2), "% WildType Wings,", x3, "% Curly Wings")
elif w1 == "WTwing" and w2 == "WTwing":
    print("Progeny Genotypes: 100 % WT/WT")
    print("Progeny Phenotypes: 100 % WildType Wings")

# Eye Color: Calculate Genotypes
y1 = ((eyes[e1])**2) * 100
y2 = (2 * ((eyes[e1] * eyes[e2]))) * 100
y3 = ((eyes[e2])**2) * 100

# Print pecerntage of phenotypes and genotypes for progeny flies
print("EYE COLOR")
if e1 == "white" and e2 == "WTeye":
    print("Progeny Genotypes:", y1, "% w/w,", y2, "% WT/w,", y3, "% WT/WT")
    print("Progeny Phenotypes:", y1, "% White Eyes,", (y2 + y3), "% WildType Eyes")
elif e1 == "white" and e2 == "white":
    print("Progeny Genotypes: 100 % w/w")
    print("Progeny Phenotypes: 100 % White Eyes")
elif e1 == "WTeye" and e2 == "white":
    print("Progeny Genotypes:", y1, "% WT/WT,", y2, "% WT/w,", y3, "% w/w")
    print("Progeny Phenotypes:", (y1 + y2), "% WildType Eyes,", y3, "% White Eyes")
elif e1 == "WTeye" and e2 == "WTeye":
    print("Progeny Genotypes: 100 % WT/WT")
    print("Progeny Phenotypes: 100 % WildType Eyes")

# Body Color: Calculate Genotypes
z1 = ((body[b1])**2) * 100
z2 = (2 * ((body[b1] * body[b2]))) * 100
z3 = ((body[b2])**2) * 100

# Print pecerntage of phenotypes and genotypes for progeny flies
print("BODY COLOR")
if b1 == "ebony" and b2 == "WTbody":
    print("Progeny Genotypes:", z1, "% e/e,", z2, "% WT/e,", z3, "% WT/WT")
    print("Progeny Phenotypes:", z1, "% Ebony Body,", (z2 + z3), "% WildType Body")
elif b1 == "ebony" and b2 == "ebony":
    print("Progeny Genotypes: 100 % e/e")
    print("Progeny Phenotypes: 100 % Ebony Body")
elif b1 == "WTbody" and b2 == "ebony":
    print("Progeny Genotypes:", z1, "% WT/WT,", z2, "% WT/e,", z3, "% e/e")
    print("Progeny Phenotypes:", (z1 + z2), "% WildType Body,", z3, "% Ebony Body")
elif b1 == "WTbody" and b2 == "WTbody":
    print("Progeny Genotypes: 100 % WT/WT")
    print("Progeny Phenotypes: 100 % WildType Body")
