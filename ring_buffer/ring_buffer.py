class RingBuffer:
	def __init__(self, capacity):
		self.capacity = int(capacity)
		self.pos      = 0
		self.buffer   = []

	def append(self, item):
		try:
			self.buffer[self.pos] = item
		except IndexError:
			self.buffer.insert(self.pos, item)
		
		if self.pos + 1 == self.capacity:
			self.pos = 0
		else:
			self.pos += 1
		
	def get(self):
		return self.buffer
