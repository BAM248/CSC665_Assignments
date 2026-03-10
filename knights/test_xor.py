from logic import *

def test():
    P = Symbol("P")
    Q = Symbol("Q")

    our_tests = [
        ({"P":False, "Q": False}, False),
        ({"P":False, "Q": True}, True),
        ({"P":True, "Q": False}, True),
        ({"P":True, "Q": True}, False),
    ]

    expression_xor = Xor(P,Q)

    for model, passable in our_tests:
        res = expression_xor.evaluate(model)
        print(f"model={model} ->{res} (expected{passable})")
        assert res == passable

    print("XOR SUCCEEDED")

if __name__ == "__main__":
    test()