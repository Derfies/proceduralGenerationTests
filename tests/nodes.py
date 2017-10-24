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

    def evaluate( self, **inputs ):
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