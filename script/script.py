import json
import re
import time

######## PARAM ############

x = 1000 # A partir de quelle conso on garde la ligne json ?
data_file_name = "data.json" # Nom du fichier avec les données json
data_output = "output.txt" # Nom du fichier de sortie

###########################

def transform(toParse):
    toParse = toParse.replace("'", "").replace("{", "").replace("}", "").replace(" ", "")
    toParse = toParse.split(',')
    toParse = toParse[9].split(':')[1]

    # Gestion erreur
    try:
        float(toParse)
    except ValueError:
        return False
    
    # On sort la ligne que si elle a une conso > XX
    if float(toParse) > x:
        return True
    return False


file = open(data_file_name, 'r', encoding="cp866")
data = json.load(file)
start = time.time()
finalString = ""

for i in data:
    if transform(str(i)):
        finalString = finalString + str(i)

text_file = open("output.txt", "w", encoding="cp866")
n = text_file.write(finalString)
text_file.close()
end = time.time()

print(finalString)
print("Finished in : " + str(end - start))
