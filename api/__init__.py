import imp
from flask import Flask, request
import os.path
from requests.sessions import session
from flask_cors import CORS, cross_origin
from scipy.optimize import linprog
import json

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def algo():

    obj = ['-25', '-27', '-27', '980']
    lhs_ineq = [
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-1, -1, -1, 0]
    ]

    rhs_ineq = [
        20,
        10,
        20,
        15,
        -5
    ]
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,)
    print(opt.x)
    print(type(opt.x.tolist()))
    return(json.dumps(opt.x.tolist()))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
