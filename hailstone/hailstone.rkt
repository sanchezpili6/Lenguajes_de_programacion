#lang racket

(define (hailstone number)
  my-list (list number)
  (cond
    [(= number 0) "Input less than 1"]
    [(= number 1) "(1)"]
    [(when (even? number) (
        (define temp (/ number 2))
        (cons temp'(my-list))
    ))
     (when (odd? number) (
        (define temp (+ (* 3 number) 1))
        (cons temp'(my-list))
     ))]
  )
)