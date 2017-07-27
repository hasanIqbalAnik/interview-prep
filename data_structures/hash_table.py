"""
One of the most important data structure in existence. Provides expected O(1) insertion, lookup, deletion.
However, if the choice of a hash function is bad, collision may often arise and this performance may degrade to
O(n) in every case.

Following is a crude implementation of a hash table, capable of storing strings.
Hash function is chosen to be the

int hash = 7;
for (int i = 0; i < strlen; i++) {
    hash = hash*31 + charAt(i);
}
taken from https://stackoverflow.com/questions/2624192/good-hash-function-for-strings?rq=1


The choice for storage is list of tuples. For example, an example hash table may look like:

32: [('australia', 12032)]
53: [('barmuda', 329), ('zimbabwe', 908)]

where, hashfunction('australia') = 32.

Time complexity:

Insertion:
if c denotes the capacity: then for the initial list creation: O(c),
hash creation is a constant time operation, O(1)
accessing the index of the list with hash value O(1)
appending at the end O(1)


Search:
Accessing the index: O(1)
searching for the item: O(n) where n is the number of words inserted so far
if a good hash function was used, this complexity is expected to be constant.

"""


class HashTable:
    def __init__(self, capacity=10000):
        """
        initialize with an optional initial size.
        """
        self.capacity = capacity
        self.table = [[] for i in xrange(capacity)]

    def compute_hash(self, word):
        """the larger the modulo number is, the more places the hash table has.
        it depends on the initial size of the hash table. """
        hash_value = 7  # some prime number
        for i in range(len(word)):
            hash_value = (hash_value * 7 + ord(word[i])) % self.capacity
        return hash_value

    def insert(self, word, value):
        """calculate the hash of the word. insert it into the hash index. if there are values
        already, append it. """
        hash_value = self.compute_hash(word)
        self.table[hash_value].append((word, value))

    def search(self, word):
        """search for the given word and return the value associated with it"""
        hash_value = self.compute_hash(word)
        tuple_list = self.table[hash_value]
        for item in tuple_list:
            if item[0] == word:
                return item[1]
        return 'item not found'


if __name__=='__main__':
    
    ht = HashTable()
    ht.insert('Russia', 17098246)
    ht.insert('Canada', 9984670)
    ht.insert('China', 9572900)
    ht.insert('USA', 9525067)
    ht.insert('Brazil', 8515767)

    print ht.search('Brazil')