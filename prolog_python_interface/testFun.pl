testFun(X) :- atom_concat('python test.py ', X, Y), shell(Y), consult('output.pl').
