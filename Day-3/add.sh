cat Fibo.sexp | guile llama.lisp/src/backend/utils/sexp-json.scm | python llama.lisp/src/backend/brilisp.py|python llama.lisp/src/backend/llvm.py > add.ll
clang add.ll Run.c
