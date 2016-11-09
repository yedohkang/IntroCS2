# hw33:  a module to provide prateLikeAPirate
# 'D. Holmes' <Mr@DavidMHolmes.net>

# a cleaned-up version of my hw28_pirate.py'

def prateLikeAPirate( civilianSpeak):
    soFar = replaceWords( normalize( Arrify( civilianSpeak)))

    # clean up spaces I inserted
    soFar = axSpaceBeforePunctuation( soFar)[1:].replace('  ',' ')
    return soFar

def Arrify( without):
    'insert Arr! after alternate sentences'
    withArrr = ''  # accumulate the result in this variable
    arrrAfterNextSentence = False

    # iterate through sentences that end in periods
    while without != '':
        endOfSentence = without.find('.') 

        if endOfSentence == -1:  # no (more) sentences in input
            withArrr += without  # accumulate the rest of the input
            without = ''         # classier: check out the "break" statement
        else:   # found another sentence. Accumulate it.
            withArrr += without[: endOfSentence + 1]  # include the period

            # Add an "Arrr!" if this sentence requires one, and update 
            # the record of the requirement.
            if arrrAfterNextSentence:
                withArrr += ' Arrr!'
            arrrAfterNextSentence = not arrrAfterNextSentence
            
            without = without[endOfSentence + 1 :]   # ax from start through period
    return withArrr
    
def normalize( original):
    'Normalize the text by inserting spaces around words.'

    # make sure there is a space at the beginning and end.
    # Note to self, added to plan: make sure extra spaces won't hurt.
    result = ' ' + original + ' '

    # pad punctuation with spaces, so they don't blend in with words
    result = result.replace('!', ' ! ')
    result = result.replace('.', ' ! ')  # Pirates be bold!  convert . to !
    result = result.replace(',', ' , ')
    result = result.replace('?', ' ? ')
    result = result.replace('\n', ' <br> ') # sentences start after newlines
    return result

def replaceWords( plain):
    'Replace some more terms, using line-continuation syntax'
    
    # Handling capitals by duplicating all the replacements is too ugly.
    # Having done it for "You", I'm putting capitals on hold until
    # I have time to do this a better way.
    
    pirateSpeak = plain.replace(' your ', ' yers ')      \
                       .replace(' you ', ' ye ')         \
                       .replace(' You ', ' Ye ')         \
                       .replace('ing ', "in' ")          \
                       .replace(' the ', " t' ")         \
                       .replace(' I ',    " me ")        \
                       .replace(' my ',   " me ")        \
                       .replace(' mine ', " me ")        \
                       .replace(' am ',  " be ")         \
                       .replace(' is ',  " be ")         \
                       .replace(' are ', " be ")         \
                       .replace("'re ",  " be ")         \
                       .replace(' myself ', " meself ")  \
                       .replace(' for ', " fer ")        \
                       .replace('ing ', "in' ")          \
                       # This comment can terminate the line continuations
    return pirateSpeak


def axSpaceBeforePunctuation( spacedOut):
    'ax spaces before punctuation, many of which I inserted'
    return spacedOut.replace(' !', '!').replace(' ,', ',').replace(' ?', '?').replace(' \n ', '\n')