# The time complexity of get is O(n)...I think
# The time complexity of append is O(1)...I think because of the length
'''
Self talk.  What do I know about ring buffers? 
I know that both the head and tail start at zero.
I know that for each piece of data inserted/appended, the head moves forward one
I know that for each piece of data consumed, the tail moves forward one.
I know that when the head and tail reach the end of the circle,
they wrap back around again to do their thing.  I'll start with this one.
'''
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  '''
  Overwrite the last (or would it be oldest?) item in storage if
  the storage is full.  So we compare the current with the storage.
  Hmmm...since capacity sets storage maybe it's comparing capacity to current?
  Either way current gets set back to 0. If not, we're adding to the current size
  '''

  def append(self, item):
    if self.current == len(self.storage):
      self.current = 0
      self.storage[self.current] = item
      self.current += 1

    else:
      self.storage[self.current] = item
      self.current += 1                             

  '''
  We can't send back a bunch of blanks.  For instance, since
  this is one big revolving circle, some of the indexes will be blank.  No data.
  Can't send back empty data. The empties have to be filtered out. Maybe call
  this safe_data. "list" can send back a sequence of data. (Yes, I had to look this up,
  as well as a number of other things). That list has to filter out the blanks. Do this from the storage.
  '''

  def get(self):
    safe_data = list(filter(None, self.storage))
    return safe_data