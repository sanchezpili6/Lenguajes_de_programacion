#lang racket
(define (tail n r)
  (if (> n 0)
    (tail (* r n) (sub1 n))
    (else r)
  )
)
