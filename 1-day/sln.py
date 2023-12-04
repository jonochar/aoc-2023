# Challenge passed. Inefficiencies in looping throug hthe lines forward and backwards when you could stop at first
# digit identified. Also probably don't need a Change Line and a Find in Line method if performance really needed to
# be evaluated, but this method made it easier to test and debug.

answer = 0
first = 0
last = 0
found = False
debug = False
part2 = True
testLoop = 100
t = 0

class Trie_Node:
    # sure we could use getters and setters... but the scope of this project is too small
    children = None
    def __init__(self) -> None:
        self.children = {}

words = {
    "one":     "1",
    "two":     "2",
    "three":   "3",
    "four":    "4",
    "five":    "5",
    "six":     "6",
    "seven":   "7",
    "eight":   "8",
    "nine":    "9",
}
trie = Trie_Node()

def print_trie(start):
    def recur(node, indent):
        return "".join(indent + key + ("$" if len(child.children) == 0 else "") + recur(child, indent + "  ") for key, child in node.children.items())
    return recur(start, "\n")

def mapWords(node, word):
    cur = node
    for c in word:
        if c not in cur.children:
            cur.children[c] = Trie_Node()
        cur = cur.children[c]

for word, num in words.items():
    mapWords(trie, word)

def checkWordValid(i, line, node, s):
    # Win Condition
    if (len(node.children) == 0):
        return s
    
    # Lose Conditions
    if (i >= len(line)):
        return ''
    
    c = line[i]
    if(c not in node.children):
        return ''
    
    return checkWordValid(i+1, line, node.children[c], s + c)

# So I almost had it... but I found an edge case such as the word "oneight"
# The more efficient thing to do is to rewrite the algorithm to search from end to beginning with reversed words, but the algorithm works for most cases in the forward direction
# So i'm just going to take the minor efficiency hit and run the alg from end to beginning without reversed words... cuz this ain't prod
# Couple hours later: New Edge case found... going forward and backwards cannot be applied to first and last
def replaceWordsWithNum(line, backwards = False):
    i = None
    end_condition = None
    incr = None

    if(backwards):
        i = len(line)
        end_condition = lambda i : (i >= 0)
        incr = -1
    else:
        i = 0
        end_condition = lambda i : (i < len(line))
        incr = 1

    while(end_condition(i)):
        string_to_replace = checkWordValid(i, line, trie, "")
        length = len(string_to_replace)
        if string_to_replace != "":
            replacement_number = words[string_to_replace]
            # Funny story that needs to be documented: As I was looking up the python method for replacing a substring, I found the "text replace" function... which would have 
            # removed the need for me to implement a Trie. I am happy to have revisted using the Trie datastructure though since it's been nearly 6 years since I took Data Struct and Algs
            line = line[:i] + replacement_number + line[i+length:]
        i += incr
    return line

def findValueInLine(l):
    found = False
    first = None
    last = None
    for c in l:
        if c.isdigit():
            c = int(c)
            if found:
                last = c
            else:
                first = c
                last = c
                found = True
    return first, last

with open("input.txt") as f:
    for l in f:
        t += 1
        if debug:
            print(l, end="")

        if part2:
            lf = replaceWordsWithNum(l, backwards=False)
            lb = replaceWordsWithNum(l, backwards=True)

        if debug:
            print(l, end="")

        first, _ = findValueInLine(lf)
        _, last  = findValueInLine(lb)
        val_in_line = first * 10 + last
        answer += val_in_line

        if debug:
            print(val_in_line)
            if t > testLoop:
                break

print("Answer is: {}".format(answer))
print("{} lines evaluated".format(t))