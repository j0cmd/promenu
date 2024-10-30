def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


#h = histogram('brontosaurus')
#print(h)


def histogram2(h):
    for i in h:
        print(h[i], i)


#histogram2(h)


d = 'prontossauros'
def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return f'dict inverse {inverse}'
    
    h = histogram('brontosaurus')
    histogram('flamengo')
    histogram2(h)


#resp = invert_dict(h)
#print(resp)
