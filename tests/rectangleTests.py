import os
import sys
import random

import nodebox.graphics as nbg

thisDirPath = os.path.dirname( os.path.abspath( __file__ ) )
uberPath = os.path.join( thisDirPath, '..' )
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


class Split( UberNode ):

    def __init__( self, *args, **kwargs ):
        UberNode.__init__( self, *args, **kwargs )

        self.addInput( 'in' )
        self.addOutput( 'out' )

    def evaluate( self, **inputs ):
        inRect = inputs['in']
        return {
            'out': Rectangle( 0, 0, inRect.width / 2, inRect.height ),
        }


class ColumnGenerator( UberNode ):

    def __init__( self, *args, **kwargs ):
        UberNode.__init__( self, *args, **kwargs )

        self.addOutput( 'outRects' )

    def evaluate( self ):

        # Generate a random number of columns with a random colour.
        rects = []
        for i in range( random.randint( 1, 9 ) ):
            colour = [0, 0, 0, 1]
            for c in range( 3 ):
                colour[c] = random.uniform( 0.0, 0.2 )
            rects.append( Rectangle( i * 50, 0, 40, 100, fill=colour ) )
        return {
            'outRects': rects,
        }


class Stack( UberNode ):

    def __init__( self, *args, **kwargs ):
        UberNode.__init__( self, *args, **kwargs )

        self.addInput( 'inRects' )
        self.addOutput( 'outRects' )

    def evaluate( self, **inputs ):
        rects = []
        for rect in inputs['inRects']:
            
            # Randomise a number of steps.
            upper = random.randint( 2, 10 )
            for i in range( 1, upper ):
                rects.append( Rectangle( rect.x, rect.y + i * 100.0 / upper, rect.width, 100.0 / upper, fill=multiplyColour( rect.fill, i / 2.0 ) ) )

        return {
            'outRects': rects
        }


if __name__ == '__main__':

    colGen = ColumnGenerator()
    colGen.doEvaluation()       # BUG - Shouldn't need to call this. Should happen automatically!
    stack = Stack()
    colGen.connect( 'outRects', stack, 'inRects' )
    rects = stack.getOutputValue( 'outRects' )

    def draw( canvas ):
        canvas.clear()
        nbg.rect( 0, 0, 500, 500 )
        for rect in rects:
            rect.draw()

    nbg.canvas.size = 500, 500
    nbg.canvas.run( draw )