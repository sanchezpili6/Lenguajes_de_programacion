#lang racket

(define alphabet (list 'a 'b 'c 'd 'e 'f 'g 'h 'i 'j 'k 'l 'm 'n 'o 'p 'q 'r 's 't 'u 'v 'x 'y 'z))

(define (shift-char letter number)
    (list-ref alphabet (+ (index-of alphabet letter) number ))
)