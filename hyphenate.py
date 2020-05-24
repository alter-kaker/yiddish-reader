import subprocess
import os
import sys

from hyphenation import yiddish_hyphenation_latex

def runerror(exception):
    if exception.stderr:
        print ( exception.stderr.decode() )
    else:
        print ( exception.stdout.decode() )
    sys.exit() 

alltexts = ''

if __name__ == '__main__':
    print('Generating hyphenation word list...')
    
    for entry in os.scandir('texts'):
        if ( not entry.is_dir()
            and os.path.splitext(entry.path)[1] == '.tex' ):
            with open(entry.path, encoding='utf-8' ) as text:
                alltexts += text.read()

    yiddish_hyphenation_latex.writeTeXfile(
            'hyphenation_list', 
            yiddish_hyphenation_latex.hyphenate(alltexts, 'viler'))
