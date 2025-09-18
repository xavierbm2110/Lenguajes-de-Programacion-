max(X,Y,X):-
    X >= Y.

max(X,Y,Y):-
    Y >= X.

reinado('Carlos II',1665,1700).
reinado('Felipe V',1700,1724).
reinado('Luis I',1724,1724).
reinado('Felipe V',1724,1746).

rige(Persona,N):- 
    reinado(Persona,A,B),
    A =< N,
    N =< B.