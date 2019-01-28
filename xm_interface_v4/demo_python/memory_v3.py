# -*- coding: utf-8 -*-
import os
import time
import cv2
import numpy as np
import ctypes as C

lib = C.cdll.LoadLibrary('../sdk/interface/libXMCamera_v4.so')


class XMIPCamera(object):
    def __init__(self, ip, port, name, password):
        self.obj = lib.XMIPCamera_init(ip, port, name, password)

    def start(self):
        lib.XMIPCamera_start(self.obj)

    def stop(self):
        lib.XMIPCamera_stop(self.obj)

    def frame(self, rows=1080, cols=1920):
        res = np.zeros(dtype=np.uint8, shape=(rows, cols, 3))
        lib.XMIPCamera_frame(self.obj, rows, cols,
                             res.ctypes.data_as(C.POINTER(C.c_ubyte)))

        return res


cp = XMIPCamera(b'10.41.0.208', 34567, b'admin', b'')

cv2.imshow("", cp.frame())
cv2.waitKey(500)
