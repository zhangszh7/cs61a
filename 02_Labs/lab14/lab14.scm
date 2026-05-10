(define (split-at lst n)
  (define (first lst n)
   (cond
    ((= n 0) nil)
    ((null? lst) nil)
    ((= n 1) (cons (car lst) nil)) 
    (else (cons (car lst) (first (cdr lst) (- n 1))))))
  
  (define (rest lst n)
   (cond
    ((= n 0) lst)
    ((null? lst) nil)
    ((= n 1) (cdr lst)) 
    (else (rest (cdr lst) (- n 1)))))
  
  (cons (first lst n) (rest lst n))
)



(define (compose-all funcs)
  (define (compose x funcs)
    (if (null? funcs) x
    (compose ((car funcs) x) (cdr funcs))))
  (lambda (x) (compose x funcs))
)

