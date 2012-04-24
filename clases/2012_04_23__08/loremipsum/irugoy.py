lorem = 'Lorem ipsum dolor sit amet consectetur adipiscing elit. Donec a mi sem, nec rhoncus sapien. Nullam ut arcu quam. Ut mollis convallis feugiat. Morbi et mi pharetra lacus fermentum varius mollis non orci. Sed pellentesque tortor ac purus scelerisque ultricies. Proin interdum eros at elit sodales in mollis orci cursus. Ut sed risus non ligula fringilla fringilla eget id neque. Nam blandit, mi tincidunt vehicula tempus, augue dui ultrices quam, ut bibendum lacus risus sit amet risus. Pellentesque vulputate est lectus, non placerat lectus.'

def strip_lorem(word_count):
    lorem_list = lorem.split()
    lorem_output = lorem_list[:word_count]
    return ' '.join(lorem_output)

def tell_me_how_many_words():
    words = input ('Enter word number: ')
    print strip_lorem (words)

tell_me_how_many_words()
