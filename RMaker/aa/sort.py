# -*- coding:utf-8 -*-
import os
import sys
input = sys.argv[1]
output = sys.argv[2]
result = []
ffo = open(input, encoding="utf8")
fo = open(output, "w", encoding="utf8")
result=list(set(ffo.readlines()))
result.sort()
fo.writelines(result)
fo.close()
ffo.close()
