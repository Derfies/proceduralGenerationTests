import nodes
from application import Application


if __name__ == '__main__':

    class ColumnApplication( Application ):

        def generateRectangles( self ):
            colGen = nodes.ColumnGenerator()
            stack = nodes.Stack()
            colGen.outputs.connect( 'rects', stack.inputs, 'rects' )
            return stack.outputs['rects']

    ColumnApplication()