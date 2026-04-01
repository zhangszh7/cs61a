
# Scheme

- call expressions and special forms
- prefix notation


## syntax

- primitive expression: `true`, `+`...
- combinations: `(+ 1 2)`

**define:**
- binding a symbol with a value: `(define x 3)`;
- define a procudure(function): `(define (f_name arg1 arg2) (expression))`

**if/cond:**
`(if <predicate> <expression>)`

**let:**
bind symbols to values temporarily(just for one expression).

**begin:**
combine several expressions together

**lambda:**
create an anonymous procedure: `(lambda (arg1 arg2) (expression))`

**quote:**
make any expression not to be evaluated,
but it can be evaluated by `eval` expression.


## data

- list: linked list
`cons`: to create a list;
`car`: returns the first element;
`cdr`: returns the rest element;
`nil`: the empty list
