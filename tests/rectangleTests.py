import nodebox.graphics as nbg

import nodes


if __name__ == '__main__':

    colGen = nodes.ColumnGenerator()
    stack = nodes.Stack()
    colGen.outputs.connect( 'rects', stack.inputs, 'rects' )

    def draw( canvas ):
        canvas.clear()
        nbg.rect( 0, 0, 500, 500 )
        for rect in stack.outputs['rects']:
            rect.draw()

    nbg.canvas.size = 500, 500
    nbg.canvas.run( draw )