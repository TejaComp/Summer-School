(brilisp 
    (define ((print int) (n int)))

    (define ((main int))
        (set (i0 int) (const 10))
        (set (i1 int) (const -11))
        (set (r1 int) (add i0 i1))
        (set (temp int) (call print r1))
        (ret temp)))

        