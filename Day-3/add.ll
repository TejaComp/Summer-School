; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"print"(i32 %".1")

define i32 @"Fibo"(i32 %"n")
{
alloca-wvennahi:
  %"n.1" = alloca i32
  %"b" = alloca i32
  %"res" = alloca i1
  %"two" = alloca i32
  %"c" = alloca i32
  %"d" = alloca i32
  %"e" = alloca i32
  %"f" = alloca i32
  %"out" = alloca i32
  br label %"entry-adrtffyx"
entry-adrtffyx:
  store i32 %"n", i32* %"n.1"
  store i32 1, i32* %"b"
  %".5" = load i32, i32* %"n.1"
  %".6" = load i32, i32* %"b"
  %"res.1" = icmp sle i32 %".5", %".6"
  store i1 %"res.1", i1* %"res"
  %".8" = load i1, i1* %"res"
  br i1 %".8", label %"l_true", label %"l_false"
l_true:
  %".10" = load i32, i32* %"n.1"
  ret i32 %".10"
l_false:
  store i32 2, i32* %"two"
  %".13" = load i32, i32* %"n.1"
  %".14" = load i32, i32* %"b"
  %"c.1" = sub i32 %".13", %".14"
  store i32 %"c.1", i32* %"c"
  %".16" = load i32, i32* %"n.1"
  %".17" = load i32, i32* %"two"
  %"d.1" = sub i32 %".16", %".17"
  store i32 %"d.1", i32* %"d"
  %".19" = load i32, i32* %"c"
  %"e.1" = call i32 @"Fibo"(i32 %".19")
  store i32 %"e.1", i32* %"e"
  %".21" = load i32, i32* %"d"
  %"f.1" = call i32 @"Fibo"(i32 %".21")
  store i32 %"f.1", i32* %"f"
  %".23" = load i32, i32* %"e"
  %".24" = load i32, i32* %"f"
  %"out.1" = add i32 %".23", %".24"
  store i32 %"out.1", i32* %"out"
  %".26" = load i32, i32* %"out"
  ret i32 %".26"
}

define void @"main"()
{
alloca-izdvsvgh:
  %"h" = alloca i32
  %"result" = alloca i32
  %"tmp" = alloca i32
  br label %"entry-adklcorh"
entry-adklcorh:
  store i32 7, i32* %"h"
  %".3" = load i32, i32* %"h"
  %"result.1" = call i32 @"Fibo"(i32 %".3")
  store i32 %"result.1", i32* %"result"
  %".5" = load i32, i32* %"result"
  %"tmp.1" = call i32 @"print"(i32 %".5")
  store i32 %"tmp.1", i32* %"tmp"
  ret void
}

