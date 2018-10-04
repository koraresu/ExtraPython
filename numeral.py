def newNumeralSystem(number):
    coll = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    second = coll.index(number)
    return [ ( coll[i] + " + " + coll[ second - i ] ) for i in range((second//2)+1)]