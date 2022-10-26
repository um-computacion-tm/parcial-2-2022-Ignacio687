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
        positionCounter = 0
        for word in compressed:
            positionCounter += 1
            try:
                key = [keys for keys in values.keys() if values[keys] == word]
                if key[0] == '':
                    self.text += ' '
                elif positionCounter == len(compressed):
                    self.text += key[0]
                else:
                    self.text += key[0]+' '
            except ValueError:
                raise CorruptedCompresion
        return self.text