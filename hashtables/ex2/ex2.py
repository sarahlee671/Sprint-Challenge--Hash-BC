#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length


    # Loop over array and add tickets to the hash table
    for x in range(length):
        hash_table_insert(hashtable, tickets[x].source, tickets[x].destination)
    
    #loop over array to find each destination after

    for y in range(length):
        #Find the first destination
        destination = hash_table_retrieve(hashtable, "NONE")
        route[y] = destination
        source = destination

    return route
