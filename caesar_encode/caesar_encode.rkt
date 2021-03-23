#lang racket

(define alphabet (list #\a #\b #\c #\d #\e #\f #\g #\h #\i #\j #\k #\l #\m #\n #\o #\p #\q #\r #\s #\t #\u #\v #\w #\x #\y #\z))
(define encoded-message "")

(define (shift-char letter number)
  (cond
    [(< (+ (index-of alphabet letter) number) 0) (list-ref alphabet (+ (+ (index-of alphabet letter) number) 26))]
    [(> (+ (index-of alphabet letter) number) 25) (list-ref alphabet (- (+ (index-of alphabet letter) number) 26))]
    [else (list-ref alphabet (+ (index-of alphabet letter) number ))]
  )
)

(define (caesar-encode message shift-num)
    (string->list message)
    (list->string(for/list ([i message])
      (shift-char i shift-num)
    ))
)

