#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_grid(op, sx, sy):
    mesh = op.appendMesh(sx, sy, closedU=False, closedV=False, addPoints=True)
    for row in range(0, mesh.numRows):
        for col in range(0, mesh.numCols):
            y = math.sin(row + 1.5) * math.cos(col)
            mesh[row, col].point.P = [row, y, col]
    # Instead of writing tdu.Position(0, 0, 1) you can also
    # use pythons list syntax:
    mesh[0, 0].prim.center = [0, 2, 0]
    return


def onCook(scriptOp):
    scriptOp.clear()
    build_grid(scriptOp, 30, 30)
    return
