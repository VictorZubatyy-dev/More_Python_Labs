class Words:
    def __init__(self):
        file_name = self.load_file("herbert1.txt", "r")
        file_name2 = self.load_file("herbert2.txt", "r")
        stop_words = self.load_file("stops.txt", "r")

        if file_name and file_name2 and stop_words:
            self.find_words(file_name, file_name2, stop_words)

    def load_file(self, file_name, flag):
        file1 = open(file_name)
        text = file1.read().strip().lower().split()
        file1.close()

        return text

    def find_words(self, file, file_2, stop_words):
        print(file)
        print(file_2)
        print(stop_words)


w = Words()