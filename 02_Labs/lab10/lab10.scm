(define (over-or-under num1 num2)
  ;(if (< num1 num2)
       ;-1
       ;(if (= num1 num2)
            ;0
            ;1
       ;)
   ;)
   (cond 
       ((> num1 num2 ) 1)
       ((= num1 num2 ) 0)
       ((< num1 num2 ) -1)
    )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


(define (make-adder num)
  ;(define (adder num1) 
    ;(+ num num1)
  ;)
  ;adder
  (lambda (num1) (+ num num1))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define (composed f g)
  ;(lambda (num) (f (g num)))
  (define (fg num) (f (g num)))
  fg
)


(define lst
  ;(list (list 1) 2 (list 3 4) 5)
   (cons (cons 1 nil) 
         (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil) )))
)


(define (remove item lst)
  (if (null? lst) 
      '()
      (let ((first (car lst))
            (rest (cdr lst)))

            (if (= first item)
                (remove item rest)
                (cons first (remove item rest))  
            )
      )
  )
)




;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

