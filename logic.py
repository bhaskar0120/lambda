### Logic in Lambda calculus

TRUE = lambda x : lambda y : x
FALSE = lambda x : lambda y : y

#----------BASIC LOGIC----------
NOT = lambda x: x(FALSE)(TRUE)
AND = lambda x: x(lambda y : y(TRUE)(FALSE))(lambda y : FALSE)
OR =  lambda x: x(lambda y: TRUE)(lambda y: y(TRUE)(FALSE)) 

# xor(X,Y) = (X or Y) and (not X or not Y)
XOR = lambda x : lambda y: AND (OR(x)(y)) (OR (NOT(x)) (NOT(y)))

# The rest of the logic can be constructed in a similar fashion as the XOR

if __name__ == "__main__":
    print("NOT")
    print(NOT(TRUE)(1)(0))
    print(NOT(FALSE)(1)(0))
    print("AND")
    print(AND(TRUE)(TRUE)(1)(0))
    print(AND(TRUE)(FALSE)(1)(0))
    print(AND(FALSE)(TRUE)(1)(0))
    print(AND(FALSE)(FALSE)(1)(0))
    print("OR")
    print(OR(TRUE)(TRUE)(1)(0))
    print(OR(TRUE)(FALSE)(1)(0))
    print(OR(FALSE)(TRUE)(1)(0))
    print(OR(FALSE)(FALSE)(1)(0))
    print("XOR")
    print(XOR(TRUE)(TRUE)(1)(0))
    print(XOR(TRUE)(FALSE)(1)(0))
    print(XOR(FALSE)(TRUE)(1)(0))
    print(XOR(FALSE)(FALSE)(1)(0))
