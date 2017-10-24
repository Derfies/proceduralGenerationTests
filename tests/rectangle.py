import nodebox.graphics as nbg


class Rectangle( object ):

    def __init__( self, x, y, width, height, fill ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill

    def draw( self ):
        rect = nbg.rect( self.x, self.y, self.width, self.height, fill=self.fill )