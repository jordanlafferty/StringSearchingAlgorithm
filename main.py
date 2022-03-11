import timeit

with open('Macbeth.txt') as f:
    line = f.read()
pattern1 = "MALCOLM"
text1 = line


def bruteForce(text, pattern):
    m = len(pattern)
    n = len(text)
    for i in range(0, n - m + 1):
        k = 0
        while k < m and text[i + k] == pattern[k]:
            k += 1
        if m == k:
            print("Pattern found at Index: ", i)


def KMP(text, pattern):
    m = len(pattern)
    n = len(text)
    for i in range(0, n - m + 1):
        dict = KMP_sub(text, pattern, i)
        if dict["pass"] is True:
            print("pattern Found at Index: ", i)
        i += dict["next"]


def KMP_sub(text, pattern, index):
    m = len(pattern)
    n = len(text)
    arr = [True] * m
    for i in range(m):
        for j in range(i + 1):
            if arr[j] is True and (index + i + j >= n or text[index + i + j] != pattern[i]):
                arr[j] = False
    dict = {
        "pass": arr[0],
        "next": m
    }
    for i in range(1, m):
        if arr[i] is True:
            dict["next"] = 1
            break
    return dict


def trie():
    pass


class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.index = []


class Trie:
    root = None

    def __init__(self):
        self.root = Node(None)

    def check(self, currNode, pattern):
        if len(pattern) == 1:
            if currNode.key == pattern[0]:
                return currNode
            else:
                return None
        else:
            if currNode.key == pattern[0] and pattern[1] in currNode.children.keys():
                newString = pattern[1:]
                return self.check(currNode.children[pattern[1]], newString)
            else:
                return None

    def search(self, pattern):
        if pattern[0] in self.root.children.keys():
            return self.check(self.root.children[pattern[0]], pattern)
        else:
            return None

    def insert(self, str, index):
        currNode = self.root
        for i in range(len(str)):
            newStr = str[:i + 1]
            if i == 0:
                found = self.search(newStr)
                if found is None:
                    node = Node(newStr)
                    currNode.children[newStr] = node
                    currNode = node
                else:
                    currNode = found
            else:
                key = str[i]
                if key in currNode.children.keys():
                    currNode = currNode.children[key]
                else:
                    node = Node(key)
                    currNode.children[key] = node
                    currNode = node
        currNode.index.append(index)

    def patchInsert(self, text, windowSize):
        n = len(text)
        for i in range(n - windowSize + 1):
            str = text[i: i + windowSize]
            self.insert(str, i)


def doTrie():
    trie1 = Trie()
    trie1.patchInsert(text1, len(pattern1))
    y = trie1.search(pattern1)
    if y is not None:
        for i in range(len(y.index)):
            print("pattern Found at Index: ", y.index[i])


print("Brute Force: ")
print(timeit.timeit('bruteForce(text1, pattern1)', 'from __main__ import bruteForce, text1, pattern1', number=1))

print("KMP: ")
print(timeit.timeit('KMP(text1, pattern1)', 'from __main__ import KMP, text1, pattern1', number=1))
# KMP(text1, pattern1)

print("Trie: ")
print(timeit.timeit('doTrie()', 'from __main__ import doTrie', number=1))
