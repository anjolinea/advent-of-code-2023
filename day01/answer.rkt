#lang racket/base
(require racket/list)
(require racket/file)


(define (get-first-digit chars)
  (cond
    [(char-numeric? (first chars)) (string->number (string (first chars)))]
    [else (get-first-digit (rest chars))]
  )
)

(define (process-string s)
  (+ (* 10 (get-first-digit (string->list s)))
           (get-first-digit (reverse (string->list s)))
  )
)

(define (part-one line ans)
  (cond
      [(eof-object? line) ans]
      [else (part-one (read-line) (+ (process-string line) ans))]
  )
)

(part-one (read-line) 0)

;; (define (part-one-inner lol ans)
;;   (cond
;;     [(empty? lol) ans]
;;     [else (part-one-inner (rest lol) (+ ans (process-string (first lol))))]
;;   )
;; )

;; (define (part-one)
;;   (part-one-inner (file->lines "input.txt") 0)
;; )
