(use-modules (ice-9 format) (ice-9 popen))

(define *angle* 0.0)
(define *x* 0.0)
(define *y* 0.0)
(define *gnuplot-pipe* #f)
(define pi 3.141592653589793)

(define (open-gnuplot)
  (set! *gnuplot-pipe* (open-output-pipe "gnuplot -persist"))
  (format *gnuplot-pipe* "set size square\n")
  (format *gnuplot-pipe* "plot '-' with lines\n"))

(define (close-gnuplot)
  (format *gnuplot-pipe* "e\n")
  (close-pipe *gnuplot-pipe*))

(define (tortoise-move length)
  (let ((new-x (+ *x* (* length (cos *angle*))))
        (new-y (+ *y* (* length (sin *angle*)))))
    (format *gnuplot-pipe* "~a ~a\n" *x* *y*)
    (set! *x* new-x)
    (set! *y* new-y)
    (format *gnuplot-pipe* "~a ~a\n" *x* *y*)))

(define (tortoise-turn angle)
  (set! *angle* (+ *angle* (* angle (/ pi 180)))))

(define (koch-line length depth)
  (if (zero? depth)
      (tortoise-move length)
      (let ((sub-length (/ length 3))
            (sub-depth (1- depth)))
        (for-each (lambda (angle)
                    (koch-line sub-length sub-depth)
                    (tortoise-turn angle))
                  '(60 -120 60 0)))))

(define (snowflake length depth sign)
  (let iterate ((i 1))
    (if (<= i 3)
        (begin
          (koch-line length depth)
          (tortoise-turn (* sign -120))
          (iterate (1+ i))))))

(define (main)
  (open-gnuplot)
  (snowflake 8 3 1)
  (tortoise-turn 180)
  (snowflake 8 3 -1)
  (close-gnuplot))

(main)


