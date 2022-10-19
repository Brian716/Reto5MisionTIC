
dictionary = ['ala', 'bervo', 'cansa']
query = ['lal', 'lal', 'sacan']

anagrams = [[]]
words = [[]]

for i in (dictionary):
    anagrams[i][i] = dictionary[i].split(',')
for i in(query):
    words[i][i] = query[i].split(',')

print(words[0][0])