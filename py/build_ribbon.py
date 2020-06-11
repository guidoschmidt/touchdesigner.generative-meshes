#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_ribbon(op, rows):
    columns = 2
    mesh = op.appendMesh(rows, columns, closedU=False, closedV=False, addPoints=True)
    # rows comes in as a parameter and defines how many rows the ribbon should
    # have. We need to iterate over a range of indices from 0 to rows:
    for row in range(mesh.numRows):
        # To get a wavy look the z coordinate is calculated
        # using the sinus function
        mesh[row, 0].point.P = [row, 0, math.sin(row)]
        mesh[row, 1].point.P = [row, 1, math.sin(row)]
    # The mesh primitive is placed onto position [0, -1, 0] in 3D space:
    mesh[0, 0].prim.center = tdu.Position(0, -1, 0)
    return


def onCook(scriptOp):
    # Clear data from the scriptOp first
    scriptOp.clear()
    build_ribbon(scriptOp, 10)
    return
