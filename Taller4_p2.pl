% Definición de los tiempos verbales
tiempo(presente).
tiempo(pasado).
tiempo(futuro).

% Definición de las personas gramaticales 
persona(primera).
persona(segunda).
persona(tercera).

% Definición de los números gramaticales
numero(singular).
numero(plural).

% Definición de la conjugación del verbo "to be"
ser(presente, primera , singular ,"am").
ser(presente, segunda , singular ,"are").
ser(presente, tercera , singular , "is").
ser(presente, primera , plural , "are").
ser(presente, segunda, plural, "are").
ser(presente, tercera, plural, "are").

ser(pasado, primera , singular ,"was").
ser(pasado, segunda , singular ,"were").
ser(pasado, tercera , singular , "was").
ser(pasado, primera , plural , "were").
ser(pasado, segunda, plural, "were").
ser(pasado, tercera, plural, "were").

ser(futuro, primera , singular ,"will be").
ser(futuro, segunda , singular ,"will be").
ser(futuro, tercera , singular , "will be").
ser(futuro, primera , plural , "will be").
ser(futuro, segunda, plural, "will be").
ser(futuro, tercera, plural, "will be").

% Conjugación del verbo "to be"
conjugar_verbo("to be", Tiempo, Persona, Numero, Conjugacion):-
    tiempo(Tiempo),
    persona(Persona),
    numero(Numero),
    ser(Tiempo, Persona, Numero, Conjugacion).

% Para otros verbos (sin conjugación especial)
conjugar_verbo(Verbo, _Tiempo, _Persona, _Numero, Verbo).

