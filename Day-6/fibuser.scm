; fib-user.s

(import (chicken foreign))
; insert actual C code
#>
  #include <math.h>
  extern int fib(int n);
  int lshift(int x, int y){
    return x << y;
  }
<#
(define xfib (foreign-lambda int "fib" int))
(print "fib(10) = " (xfib 10))
