from graphicsInterface import Graphicsinterface
from pokerapp import PokerApp
from textInterface import TextInterface
# inter = TextInterface()
inter=Graphicsinterface()
app = PokerApp(inter)
app.run()