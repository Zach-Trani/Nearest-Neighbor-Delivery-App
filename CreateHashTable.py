class CreateHashMap:
    # initialize an empty list of buckets
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # insert function - inserts a new item into hash table
        # citing source - "C950 - Webinar 1 - Let's Go Hashing - Complete Python Code"
    def insert(self, key, item):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # update key if it is already existing in bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True
            
        # if key does not exist, insert item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
    
    # lookup function - retrieve a value associated with a key
    def lookup(self, key):
        # determine the respective keys bucket
        hash_index = hash(key) % len(self.list)
        hash_chain = self.list[hash_index]

        # return the matching item on key match
        for kv_pair in hash_chain:
            if kv_pair == kv_pair[0]:
                return kv_pair[1]
        return None

    # delete function - deletes a item in hash table
    def delete(self, key):
        hash_index = hash(key) % len(self.list)
        hash_chain = self.list[hash_index]

        # remove the key from the list if it exists
        if key in hash_chain:
            hash_chain.remove(key)
