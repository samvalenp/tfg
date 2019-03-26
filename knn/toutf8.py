import codecs


filename = 'result.csv'

with codecs.open(filename, 'r') as f:
    text = f.read()
# process Unicode text
with codecs.open('hola.csv', 'w', encoding='utf8') as f:
    f.write(text)