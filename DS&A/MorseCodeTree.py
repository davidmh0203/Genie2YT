from tree import BTNode

table = [('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
    ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
    ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
    ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
    ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
    ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
    ('Y', '-.--'),  ('Z', '--..')]
def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]
def decode_simple(morse):
    for tp in table:
        if morse == tp[1]:
            return tp[0]

def make_morse_tree():
    root = BTNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left ==None:
                    node.left = BTNode(None,None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = BTNode(None,None,None)
                node = node.right
        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.': node = node.left
        elif c =='-': node = node.right
    return node.data







morseCodeTree = make_morse_tree()
str = input("입력 문장: ") # G A M E O V E R
mlist = []

for ch in str:
    code = encode(ch)
    mlist.append(code)

print("Morse Code: ", mlist)
print("Decoding: ", end='')

for code in mlist:   # ['..', '.-', '..--']
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()
