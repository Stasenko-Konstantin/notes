# Guy L. Steele Jr. and Gerald Jay Sussman - the art of the interpreter or, the modularity complex (parts zero, one and two)

модуль - независимая часть программы
Наиболее юазебльный (useful) модуль тот, что обладает ссылочной прозрачностью.

S-выражения - в нашем случае будут пониматься неформально и неполно как множество атомов и списков.
Атом - "неделимый" объект записываемый строкой символов и цифр. Если используются только
цифры, то атом интерпретируется как число. Некоторые специальные символы интерпретируются
как символы, например "-" и "+".
Список - (возможно пустая) последовательность S-выражений, в которой S-выражения записываются
по порядку между множеством скобок и разделенные пробелами. Например список атомов "FOO", "43"
и "BAR" будет записан как "(FOO 43 BAR)". Стоит отметить что определение списка - рекурсивно,
т.е. список может содержать в себе другие списки. Например:

```scheme
(DEFINE (SECOND X) (CAR (CDR X)))
```

[Я бы описал это следующей псевдограмматикой (не факт что верной): ]
```antlrv4
sexp ::= atom | list
atom ::= a-zA-Z0-9 | +-=_ ...
list ::= '(' sexp ')'
```

Нам нужно несколько процедур для различения, декомпозиции и конструирования S-выражений.
Предикат ATOM примененный к S-выражению возвращает истину если ему передан атом и ложь 
в других случаях. Пустой список принимается за атом. Предикат NULL истинен только на пустом
списке. Предикат NUMBERP истинен на числах и ложен на атомах и списках. Предикат EQ 
примененный к двум атомам истинен, если они идентичны, ложен, когда он применен на атоме
и любом другом S-выражении. (Мы пока не определили EQ на двух списках. Это будет важно 
когда разговор зайдет о side-эффектах)

---

