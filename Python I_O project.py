import itertools
import os
import warnings

warnings.filterwarnings('ignore')

try:
    mofe = input(''' Input the name of the file
                    #  which you would like to be read
    ''')

    n_lines = int(input("How many lines of this file will you like to be read?"))


    def read(mofe, n_lines):
        teni = open(mofe)
        from itertools import islice
        with teni as f:
            for line in islice(f, n_lines):
                print(line)
    read(mofe, n_lines)


except os.UnknownValueError:
    # Check for unknown errors
    print('I do not understand what you said. Please repeat your words slowly')
except os.RequestError as e:
    b = str(e)
    print('Request results from Google Speech Recognition service error: ' + b)


