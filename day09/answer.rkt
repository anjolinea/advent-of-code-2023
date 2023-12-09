#lang racket/base
(require racket/file)
(require racket/string)
(require srfi/1)

;; Helper functions
(define (differences lon)
  (drop-right (map - (append (cdr lon) '(0)) lon) 1)
)

(define (list-equel? lst)
  (apply = lst))
  
(define (all-zeroes? lst)
  (list-equel? (cons 0 lst))
)

(define (process-one lon)
  (cond 
    [(all-zeroes? lon) 0]
    [else (+ (last lon)(process-one (differences lon)))]
  )
)

(define (process-two lon)
  (cond 
    [(all-zeroes? lon) 0]
    [else (- (first lon) (process-two (differences lon)))]
  )
)

;; Answers
(define (part-one line ans)
  (cond
      [(eof-object? line) ans]
      [else (part-one (read-line) (+ (process-one (map string->number (string-split line))) ans))]
  )
)

(define (part-two line ans)
  (cond
      [(eof-object? line) ans]
      [else (part-two (read-line) (+ (process-two (map string->number (string-split line))) ans))]
  )
)

(part-two (read-line) 0)