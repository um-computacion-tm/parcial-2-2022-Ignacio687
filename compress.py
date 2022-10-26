class CorruptedCompresion(Exception):
    pass

class Compress():
    
    def __init__(self):
        self.values = {}
        self.compressed = []
        self.text = ''

    def compress(self, text):
        text += ' '
        keyCounter = 0
        statement = ''
        for word in text:
            if word != ' ':
                statement += word
            else:
                if statement in self.values.keys():
                    self.compressed.append(self.values[statement])
                    statement = ''
                else: 
                    keyCounter += 1
                    self.values[statement] = keyCounter
                    self.compressed.append(keyCounter)
                    statement = ''
        return self.compressed, self.values

    def uncompress(self, compressed, values):
        for word in compressed:
            try:
                if values.index(word) == '':
                    self.text += ' '
                else:
                    self.text += values.index(word)
            except ValueError:
                raise CorruptedCompresion