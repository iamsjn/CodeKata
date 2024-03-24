class StringFrequency:

    def __init__(self):
        self.frequency = [0]*26

    def __get_hash(self, char):
        return ord(char) - ord('a')

    def get_frequency(self, word):
        for i in word:
            index = self.__get_hash(i)
            if(index != None):
                self.frequency[index] = self.frequency[index] + 1

        print(str(self.frequency))

    def get_frequency2(self, word):
        frequency = {}
        for i in word:
            if i in frequency:
                frequency[i] = frequency[i] + 1
            else:
                frequency[i] = 1

        print(frequency)


if __name__ == "__main__":
    stringFrequency = StringFrequency()
    stringFrequency.get_frequency('aabbds')
    stringFrequency.get_frequency2('aabbds')
