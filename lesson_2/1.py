s = 'Hello, World!!'
chars = {'!', ','}
res = s.translate(str.maketrans('', '', chars))
print(res)  # Hello World