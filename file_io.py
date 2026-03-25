FILE_NAME="input.txt"

def read_greeting():
    greeting_file=open(FILE_NAME, 'r')
    _content=greeting_file.read()
    return _content

if __name__=='__main__':
    print(read_greeting())