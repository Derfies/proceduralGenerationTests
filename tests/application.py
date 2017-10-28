import nodebox.graphics as nbg


class Application( object ):

    def __init__( self, width=500, height=500 ):
        nbg.canvas.width = width
        nbg.canvas.height = height
        self.rects = self.generateRectangles()

        def draw( canvas ):
            keys = canvas.keys
            if 'f5' in keys:
                self.rects = self.generateRectangles()
            canvas.clear()
            nbg.rect( 0, 0, canvas.width, canvas.height )
            for rect in self.rects:
                rect.draw()

        nbg.canvas.run( draw )

    def generateRectangles( self ):
        return []