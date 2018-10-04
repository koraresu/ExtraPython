import re
number = ['0','1','2','3','4','5','6','7','8','9']

def get_number_letter(n):
    global number
    num,letter    = "",""
    for i in range(len(n)):
        if n[i] in number:
            num += n[i]
        else:
            letter += n[i]
    return(int(num),letter)
def decodeString(s):
    z = s
    if '[' in s:
        if ']' not in s:
            s += ']'
        x = ""
        y = ""
        for n,d in re.findall(r'(.*?)\[(.*?)\]',s):
            y += n+"["+d+"]"
            num,letter = get_number_letter(n)
            d = decodeString( d )
            x += letter+( d * int(num ) )
        z = l
        #z = ""
        return x+z
    else:
        return s

print( decodeString('2[b3[a]]') )
print( decodeString('4[ab]') )
print( decodeString('z1[y]zzz2[abc]') )
print( decodeString('2[abc]3[cd]ef') )
