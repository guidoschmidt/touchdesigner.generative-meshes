#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_globe(op, sx, sy):
    mesh = op.appendMesh(sx, sy, closedU=True, closedV=False, addPoints=True)
    radius = 10
    # In order to prevent connection between north and south pole
    # of the globe mesh, we need to iterate only up to numRows - 1
    row_count = mesh.numRows - 1
    col_count = mesh.numCols
    for row in range(mesh.numRows):
        lat = (row / row_count) * math.pi - (math.pi / 2)
        for col in range(mesh.numCols):
            lng = (col / col_count) * math.pi * 2 - math.pi
            x = radius * math.cos(lng) * math.cos(lat)
            y = radius * math.sin(lng) * math.cos(lat)
            z = radius * math.sin(lat)
            mesh[row, col].point.P = [x, y, z]
    mesh[0, 0].prim.center = [0, 0, 0]
    return


def onCook(scriptOp):
    scriptOp.clear()
    build_globe(scriptOp, 50, 50)
    return
