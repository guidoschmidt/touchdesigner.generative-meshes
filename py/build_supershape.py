#!/usr/bin/env python
# -*- coding: utf-8 -*-

def supershape(theta, m, n1, n2, n3):
    a = 1
    b = 1
    t1 = abs((1 / a) * math.cos(m * theta / 4))
    t1 = math.pow(t1, n2)
    t2 = abs((1 / b) * math.sin(m * theta / 4))
    t2 = math.pow(t2, n3)
    t3 = t1 + t2
    r = math.pow(t3, -1 / n1)
    return r


def build_supershape(op, sx, sy):
    m = 202.0
    n1 = 5.1
    n2 = 3.0
    n3 = 7.2
    lng_rng = math.pi 
    lat_rng = math.pi * 2
    mesh = op.appendMesh(sx, sy, closedU=False, closedV=False, addPoints=True)
    radius = 10
    row_count = mesh.numRows - 1
    col_count = mesh.numCols - 1
    for row in range(mesh.numRows):
        lat = (row / row_count) * lng_rng  - (lng_rng / 2)
        r2 = supershape(lat, m, n1, n2, n3)
        for col in range(mesh.numCols):
            lng = (col / col_count) * lat_rng - (lat_rng / 2)
            r1 = supershape(lng, m, n1, n2, n3)
            x = radius * r1 * math.cos(lng) * math.cos(lat)
            y = radius * r1 * math.sin(lng) * math.cos(lat)
            z = radius * r2 * math.sin(lat)
            mesh[row, col].point.P = [x, y, z]
    mesh[0, 0].prim.center = [0, 0, 0]
    return


def onCook(scriptOp):
    scriptOp.clear()
    build_supershape(scriptOp, 50, 50)
    return
