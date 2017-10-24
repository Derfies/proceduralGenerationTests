import nodebox.graphics as nbg


class Application( object ):

    def __init__( self ):
        self.rects = self.generateRectangles()
        nbg.canvas.size = 500, 500

        def draw( canvas ):
            keys = canvas.keys
            if 'f5' in keys:
                self.rects = self.generateRectangles()
            canvas.clear()
            nbg.rect( 0, 0, 500, 500 )
            for rect in self.rects:
                rect.draw()

        nbg.canvas.run( draw )

    def generateRectangles( self ):
        return []