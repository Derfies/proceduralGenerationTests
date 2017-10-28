import nodebox.graphics as nbg

import nodes
from rectangle import Rectangle
from application import Application


if __name__ == '__main__':

    class QuadTree( Application ):

        def generateRectangles( self ):
            quad = nodes.Quad()
            quad.inputs['rects'] = [
                Rectangle( 
                    0, 
                    0, 
                    nbg.canvas.width, 
                    nbg.canvas.height, 
                    fill=(1, 0, 0, 1) 
                )
            ]
            return quad.outputs['rects']

    QuadTree()