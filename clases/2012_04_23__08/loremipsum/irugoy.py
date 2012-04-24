lorem = 'Lorem ipsum dolor sit amet consectetur adipiscing elit. Donec a mi sem, nec rhoncus sapien. Nullam ut arcu quam. Ut mollis convallis feugiat. Morbi et mi pharetra lacus fermentum varius mollis non orci. Sed pellentesque tortor ac purus scelerisque ultricies. Proin interdum eros at elit sodales in mollis orci cursus. Ut sed risus non ligula fringilla fringilla eget id neque. Nam blandit, mi tincidunt vehicula tempus, augue dui ultrices quam, ut bibendum lacus risus sit amet risus. Pellentesque vulputate est lectus, non placerat lectus.'

def stripLorem(wordCount):
    loremList = lorem.split()
    loremOutput = loremList[:wordCount]
    return ' '.join(loremOutput)

def tellMeHowManyWords():
    words = input ('Enter word number: ')
    print stripLorem (words)

tellMeHowManyWords()
