

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Hashtable:

    def __init__(self, size =1024):
        self.size = size
        self.bucket = size * [None]     # initializes with buckets of list size None, creates the table

#-----------------------------------------------------------------

    def add(self, key, value):
        pass


# add/set
# function purpose- computes index of the key using hash function, puts key/value into the hash table
# Determine what index the key/value pair should be placed in the hash table.
# Go to that index. See what's in the bucket at that index.
#    if bucket is empty, create new node and add it there
#    if bucket has a linked list with at least one node(a key/value pair), iterate to the end of the list and add a new key there
# -------
# Arguments: key, value
# Returns: nothing
# This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
# Should a given key already exist, replace its value from the value argument given to this method.

#-----------------------------------------------------------------

    def get(self, key):
        pass


# find
# function purpose- grabs a data value stored in a given key
#   uses the hash function to get the index for a given key
#   go to the bucket for that index
#   iterate nodes in that bucket/linked list until key is found or until end of list
#   returns value of the found key or none if not found
# --------
# Arguments: key
# Returns: Value associated with that key in the table

#-----------------------------------------------------------------

    def contains(self):
        pass



# function purpose- checks table if a key exists or not
# Arguments: key
# Returns: A boolean indicating if the key exists in the table already.

#-----------------------------------------------------------------

    def hash(self, key):

        sum = 0
        for character in key:           # iterate through every item in the key
            sum += ord(character)       #converts to ascii, adds to a variable
        primed = sum * 23               # variable multiplied by prime number
        index = primed % self.size
        return index


# function purpose- converts key into a bucket index aka performs a "hash"
# key portion of the key/value pair is hashed
#   iterate through every item in the key
#   convert to ascii, add it to a variable
#   variable is then multiplied by a prime number
#   convert result into an index, will then be taken and run the modulus on size of the hash map
# -------
# Arguments: key
# Returns: Index in the collection for that key

#-----------------------------------------------------------------

    def keys(self):
        pass

# Returns: Collection of keys

#-----------------------------------------------------------------
