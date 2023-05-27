text = input('''Enter your text here: \n >''')
for i in range(len(text)):
    if '(' in text:
        opening = True
        start = text.index('(')
    else:
        opening = False
    if ')' in text:
        close = True
        stop = text.index(')')
    if opening == close:
        text = text[:start] + text[stop + 1:]
        continue
print(text)
