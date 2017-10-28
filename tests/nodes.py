import os
import sys
import random

thisDirPath = os.path.dirname( os.path.abspath( __file__ ) )
uberPath = os.path.join( thisDirPath, '..', '..', 'uberNode' )
if uberPath not in sys.path:
    sys.path.append( uberPath )
import utils
from uberNode import UberNode
from rectangle import Rectangle


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

    def evaluate( self ):
        rects = []
        for rect in self.inputs['rects']:
            
            # Randomise a number of steps.
            upper = random.randint( 2, 10 )
            for i in range( 1, upper ):
                rects.append( Rectangle( 
                    rect.x, 
                    rect.y + i * 100.0 / upper, rect.width, 
                    100.0 / upper, 
                    fill=utils.multiplyColour( rect.fill, i / 2.0 ) 
                ) )

        self.outputs['rects'] = rects


class Quad( UberNode ):

    def __init__( self ):
        UberNode.__init__( self, inputs={'rects': []}, outputs={'rects': []} )

    def evaluate( self ):
        outRects = []
        
        def splitRect( rect ):

            r = random.uniform( 0.0, 1.0 )
            g = random.uniform( 0.0, 1.0 )
            b = random.uniform( 0.0, 1.0 )

            xs = [
                rect.x, 
                rect.x + rect.width / 2.0,
                rect.x,
                rect.x + rect.width / 2.0,
            ]
            ys = [
                rect.y, 
                rect.y,
                rect.y + rect.height / 2.0,
                rect.y + rect.height / 2.0,
            ]

            return [Rectangle( 
                    xs[i] + 20, 
                    ys[i] + 20, 
                    rect.width / 2.0 - 40, 
                    rect.height / 2.0 - 40, 
                    fill=(r, g, b, 1) 
                ) for i in range( len( xs ) )]

        def recRect( rects, count=0 ):
            if count > 2: 
                return
            for rect in rects:
                outRects.append( rect )
                newRects = splitRect( rect )
                outRects.extend( newRects )
                recRect( newRects, count + 1 )
        
        recRect( self.inputs['rects'] )
        self.outputs['rects'] = outRects