from graphics import *
from button import Button

class MaxYDialog:
	"""
	A custom window for getting simulation values (angle, velocity, and height) from the user.
	"""
	def __init__ (self, maxheight):
		"""
		Build and display the maxheight windxow
		"""
		self.win =win = GraphWin("Maximum Height", 200, 175)
		win.setCoords(0,4.5,4,.5)

		Text(Point(2,1), "Maximum Height :").draw(win)
		Text(Point(2,2.3), str(maxheight)).draw(win)

		self.OK = Button(win, Point(2, 3.6), 1.25, 1, "OK")
		self.OK.activate()



	def close(self):
		"""
		close the input window
		"""
		self.win.close()