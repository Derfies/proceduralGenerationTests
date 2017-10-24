import os
import sys
import random

import nodebox.graphics as nbg

thisDirPath = os.path.dirname( os.path.abspath( __file__ ) )
uberPath = os.path.join( thisDirPath, '..', '..', 'uberNode' )
if uberPath not in sys.path:
    sys.path.append( uberPath )
from uberNode import UberNode


def multiplyColour( c, d ):
    return [
        c[0] * d,
        c[1] * d,
        c[2] * d,
        1
    ]


class Rectangle( object ):

    def __init__( self, x, y, width, height, fill ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill

    def draw( self ):
        rect = nbg.rect( self.x, self.y, self.width, self.height, fill=self.fill )


class ColumnGenerator( UberNode ):

    def __init__( self  ):
        UberNode.__init__( self, outputs={'rects': []} )

    def evaluate( self ):

        # Generate a random number of columns with a random colour.
        rects = []
        for i in range( random.randint( 1, 9 ) ):
            colour = [0, 0, 0, 1]
            for c in range( 3 ):
                colour[c] = random.uniform( 0.0, 0.2 )
            rects.append( Rectangle( i * 50, 0, 40, 100, fill=colour ) )
        self.outputs['rects'] = rects


class Stack( UberNode ):

    def __init__( self ):
        UberNode.__init__( self, inputs={'rects': []}, outputs={'rects': []} )

    def evaluate( self, **inputs ):
        rects = []
        for rect in self.inputs['rects']:
            
            # Randomise a number of steps.
            upper = random.randint( 2, 10 )
            for i in range( 1, upper ):
                rects.append( Rectangle( rect.x, rect.y + i * 100.0 / upper, rect.width, 100.0 / upper, fill=multiplyColour( rect.fill, i / 2.0 ) ) )

        self.outputs['rects'] = rects


if __name__ == '__main__':

    colGen = ColumnGenerator()
    stack = Stack()
    colGen.outputs.connect( 'rects', stack.inputs, 'rects' )

    def draw( canvas ):
        canvas.clear()
        nbg.rect( 0, 0, 500, 500 )
        for rect in stack.outputs['rects']:
            rect.draw()

    nbg.canvas.size = 500, 500
    nbg.canvas.run( draw )