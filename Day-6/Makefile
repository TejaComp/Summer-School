# Basic Makefile for the tortoise package.

CFLAGS = `pkg-config --cflags guile-3.0`
LIBS = `pkg-config --libs guile-3.0`

.PHONY: clean build run

build: tortoise

clean:
	rm -f tortoise tortoise.o

run: tortoise
	./tortoise

tortoise: tortoise.o
	gcc $< -o $@ $(LIBS)

tortoise.o: tortoise.c
	gcc -c $< -o $@ $(CFLAGS)

