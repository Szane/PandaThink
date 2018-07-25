from flask import Flask
import numpy as np
import KM
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    km = KM.KMArithmetic()
    weight = [[1, 2, 3],
              [1, 3, 2],
              [2, 3, 1]]
    v = km.bestmatch(3, 3, weight)
    m = km.getmatch()
    print(m)
    print(str(v))

    return '1'

if __name__ == '__main__':
    app.run()
