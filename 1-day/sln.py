
answer = 0
first = 0
last = 0
found = False
debug = False
testLoop = 5
t = 0

class Trie_Node:
    # sure we could use getters and setters... but the scope of this project is too small
    val = None
    next = {}

words = [
    ["one", 3, 1],
    ["two", 3, 2],
    ["six", 3, 6],
    ["four", 4, 4],
    ["five", 4, 5],
    ["nine", 4, 9],
    ["three", 5, 3],
    ["seven", 5, 7],
    ["eight", 5, 8],
]
trie = Trie_Node()

for word in words:
    

# This is the many loops method... i feel like there's a better way to do this with recursion. I'm just rusty
def CheckForValidWords(start, n_chars, line, words):
    good_idx = [range(0, len(words))]
    bad_idx = []

    for c in range(0, n_chars):
        for w in range(0, len(good_idx)):
            if words[w, 0][c] != line[start + c]:
                bad_idx.append(w)
        for b in bad_idx:
            good_idx.remove(b)

    return good_idx

with open("input.txt") as f:
    for l in f:
        found = False
        for i in range(0, len(l)):
            if c.isdigit():
                continue
            
            if CheckForValidWords(i, l, words):

        if debug:
            if t > testLoop:
                break
            else:
                t += 1
            print(first*10 + last)

        answer += first * 10 + last

print("Answer is: {}".format(answer))