import operator

from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


def eval_expression(expr):
    if expr is None:
        return None
    operators = set("+-*/")
    op_found = []
    num_found = []
    num_buff = []
    for c in expr:
        if c in operators:
            num_found.append("".join(num_buff))
            num_buff = []
            op_found.append(c)
        else:
            num_buff.append(c)
    num_found.append("".join(num_buff))

    operators_order = ("*/", "+-")

    op_dict = {
        "*": operator.mul,
        "/": operator.truediv,
        "+": operator.add,
        "-": operator.sub,
    }

    for op in operators_order:
        while any(o in op_found for o in op):
            idx, oo = next((i, o) for i, o in enumerate(op_found) if o in op)
            op_found.pop(idx)
            values = map(float, num_found[idx : idx + 2])
            value = op_dict[oo](*values)
            num_found[idx : idx + 2] = [value]

    return num_found[0]


@app.route("/", methods=["POST", "GET"])
def math_js():
    if request.method == "POST":
        return {"result": eval_expression(request.data.get("expr"))}
    elif request.method == "GET":
        return {"result": eval_expression(request.args.get("expr"))}
    else:
        return None


if __name__ == "__main__":
    app.run(debug=True)
