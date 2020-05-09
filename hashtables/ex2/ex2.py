#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # start at source none
    # ticket.destination = next
    # find next in source.keys()
    # next_dest =  source.destination
    route = []
    cache = {}
    for i in range(length):
        new_tup = {tickets[i].source: tickets[i].destination}
        cache.update(new_tup)
    nextD = cache['NONE']
    destination = nextD
    while destination != 'NONE':
        destination = nextD
        route.append(destination)
        nextD = cache[nextD]

    return route
