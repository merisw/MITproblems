# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) < 2:
        return aStr
    elif len(aStr) == 2:
        return aStr[1] + aStr[0]
    elif len(aStr) > 2:
        return aStr[-1] + reverseString(aStr[:-1])
    
#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    elif len(x) == 1:
        if x in word:
            return True
        else:
            return False
    elif len(x) > 1:
        if x[0] in word:
            partWord = word.partition(x[0])
            return x_ian(x[1:], partWord[2])
        else:
            return False
            
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    def insertNewlinesRec(text, lineLength):
        if text[lineLength - 1] == ' ':
            return lineLength - 1
        else:
            return 1 + insertNewlinesRec(text[1:], lineLength)
        
    if len(text) <= lineLength:
        return text
    elif ' ' not in text[lineLength - 1:]:
        return text
    else:
        spot = insertNewlinesRec(text, lineLength)  
        return text[:spot] + '\n' + insertNewlines(text[spot + 1:], lineLength)
        
