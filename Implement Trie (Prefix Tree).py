#Time Complexity:: O(l) - (for all three operations), maximum length of words, because you traverse each character at a time
#Space Complexity:: O(n*l) - none of the word have common prefixes, n is the number of words
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class TrieNode: #creating a trie node constructor
    def __init__(self): #trie node has following attributes
        self.isEnd = False #this is a flag to spot the end of a word. if this is True then there is a word ending at this trie node
        self.children = [None]*26 #children are the characters in the alphabet
class Trie(object):

    def __init__(self):
        self.root = TrieNode() #initializing the first root trie node

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root #using a current node to traverse the characters
        for char in word: #for each character in the word
            key = ord(char) - ord('a') #find the key of the character by subtracting ascii value of lowercase 'a'
            if curr.children[key]==None: #if the current.children[key] is empty then add a new TrieNode with a new array of children node characters
                curr.children[key]= TrieNode() #create trie node( a new character)
            curr = curr.children[key] #the character slot has a node then traverse into it till you reach an empty index
        curr.isEnd = True #set the end to true after inserting the new word/characters

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root #use a curr node to traverse the trie
        for char in word: #for each character in the word
            key = ord(char)-ord('a') #find the key for the character
            if curr.children[key]==None: #if the index for the character is empty then return False 
                return False
            curr = curr.children[key] #move the current pointer to the next node, to move to the next character
        return curr.isEnd #if there is no words in the trie or if the word doesn't exist then return the isEnd(Imp***)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root #use a curr node to traverse the trie
        for char in prefix: #check the characters of a prefix not the word
            key = ord(char) - ord('a') #find the key for the character
            if curr.children[key]==None: #if the index for that character is empty then return false
                return False
            curr = curr.children[key] #keep moving the pointer to the next node(character) till all the prefix characters have been seen
        return True #when all characters are present and the for loop completes successfully then return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)