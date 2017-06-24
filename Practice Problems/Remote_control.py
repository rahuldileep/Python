class remote_control:
	def __init__(self):
		self.channels=['ESPN','Star Sports','M.Tv','V Channel']
		self.index=-1
	def __iter__(self):
		return self


	def next(self):
		try:
			self.index=self.index+1
			return self.channels[self.index]

		except IndexError:
			print 'Out of Channels'
r=remote_control()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))





