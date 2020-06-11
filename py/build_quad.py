#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_quad(op):
    # Append a mesh to the ScriptSOP operator, that contains 2 rows and 2 colums
    rows = 2
    columns = 2
    mesh = op.appendMesh(rows, columns, closedU=False, closedV=False, addPoints=True)
    # Now set the coordinates of the meshs points
    mesh[0, 0].point.P = [+1, +1, 0]
    mesh[0, 1].point.P = [-1, +1, 0]
    mesh[1, 0].point.P = [+1, -1, 0]
    mesh[1, 1].point.P = [-1, -1, 0]
    # You can set the mesh primitives center to a 3d position
    mesh[0, 0].prim.center = tdu.Position(0, 1, 0)
    return


def onCook(scriptOp):
    # Clear data from the scriptOp first
    scriptOp.clear()
    # Call our build_quad function to generate the quad mesh
    build_quad(scriptOp)
    return
