###### --------------------------------------------
## The author of these scripts is T. D. Devlin 
###### --------------------------------------------

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# auxiliary symbols for puzzle 3 (what A actually said)
ASaidKnight = Symbol("A said 'I am a knight'")
ASaidKnave = Symbol("A said 'I am a knave'")

# Puzzle 1
# A says "I am both a knight and a knave."
# ----------------------------------------
##   write the statement(s) in PL 
# Statement from A
statement1 = And(AKnight, AKnave)
##   Fill in the knowledge base
knowledge1 = And(
    # A must be either a knight or a knave (but not both)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # knights tell the truth, knaves lie
    Biconditional(AKnight, statement1)
)
# ----------------------------------------

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# ----------------------------------------
##   write the statement(s) in PL 
# A's statement: the two are same kind
statementA2 = Biconditional(AKnight, BKnight)
# B's statement: the two are different kinds
statementB2 = Xor(AKnight, BKnight)
##   Fill in the knowledge base
knowledge2 = And(
    # each person is either knight or knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # honesty constraints
    Biconditional(AKnight, statementA2),
    Biconditional(BKnight, statementB2)
)
# ----------------------------------------

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# ----------------------------------------
##   write the statement(s) in PL 
# we introduce auxiliary symbols to record what A actually said
# (only one of these will be true)

# Expression representing what A said as a formula
statementA3 = Or(And(ASaidKnight, AKnight), And(ASaidKnave, AKnave))

# B's combined statement (both parts together):
#   "A said 'I am a knave'" AND "C is a knave"
statementB3 = And(ASaidKnave, CKnave)

# C's statement
statementC3 = AKnight

##   Fill in the knowledge base
knowledge3 = And(
    # each person is either a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # exactly one of the auxiliary statements is true
    Or(ASaidKnight, ASaidKnave),
    Not(And(ASaidKnight, ASaidKnave)),

    # honesty constraints linking each person to their statements
    Biconditional(AKnight, statementA3),
    Biconditional(BKnight, statementB3),
    Biconditional(CKnight, statementC3)
)
# ----------------------------------------


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
