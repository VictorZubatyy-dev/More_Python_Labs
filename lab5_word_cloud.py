# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-22
# author: B. Schoen-Phelan
# date: Oct 2021
# purpose: Lab 5 Exceptions and Files

class WordCloud:
    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict, self.text = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict, self.text)


    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html

    def create_html(self, the_dict, text):
        the_dict = self.add_to_dict(text, the_dict)
        print(the_dict)
        fo = open("output.html", "w")
        fo.write(f'<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')
        # your code goes here!
        for word in the_dict:
            font_size = the_dict[word] * 10
            fo.write(f'<span style="font-size: {font_size}px"> {word} </span>')
        fo.write('</div>\
            </body>\
            </html>')
        fo.close()

    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}
        file = open('gettisburg.txt', 'r')
        text = file.read().strip().lower().split()
        # set the values to 0
        for word in text:
            my_dict[word] = 0
        return my_dict, text
        # your code goes here:


    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, new_text, my_dict):
        # search through each word
        for word in new_text:
            # if word matches key add 1 to key's value
            if word in self.my_dict:
                my_dict[word] += 1
        return my_dict


# creates an instance of the WordCloud object
# remember first step after creation of an instance
# is that Python goes into the __init__ function
wc = WordCloud()


