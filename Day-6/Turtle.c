#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <math.h>


//Create Static constant variables width and height
static const int WIDTH = 10;
static const int HEIGHT = 10;

//Create a File pointer
static FILE*

//Create a function to create a gnuplot
start_gnuplot ()
{
// We create an output point to access array pipes of 2 paths.
  FILE* output;
  int pipes[2];
  pid_t pid; //A process identification variable pid created to identify the process id

  pipe(pipes); // We are pipelining the 2 process i.e parent and child into a single line
  pid = fork(); //We create a new child process
    

  if (!pid)
  {
    dup2(pipes[0], STDIN_FILENO);
    execlp("gnuplot", NULL);
    return NULL; /* Not reached. */
  }

  output = fdopen(pipes[1], "w");

  fprintf(output, "set multiplot\n");
  fprintf(output, "set parametric\n");
  fprintf(output, "set xrange [-%d:%d]\n", WIDTH, WIDTH);
  fprintf(output, "set yrange [-%d:%d]\n", HEIGHT, HEIGHT);
  fprintf(output, "set size ratio -1\n");
  fprintf(output, "unset xtics\n");
  fprintf(output, "unset ytics\n");
fflush(output);

  return output;
}

static FILE* global_output;

static void
draw_line (FILE* output, double x1, double y1, double x2, double y2)
{
  fprintf(output, "plot [0:1] %f + %f * t, %f + %f * t notitle\n",
          x1, x2 - x1, y1, y2 - y1);
  fflush(output);
}

/*int main() {
    // Start gnuplot
    global_output = start_gnuplot();
    if (global_output == NULL) {
        fprintf(stderr, "Error: Failed to start gnuplot\n");
        return 1;
    }

    // Draw a line from (0, 0) to (5, 5)
    draw_line(global_output, 0, 0, 5, 5);

    // Pause to see the plot
    printf("Press Enter to exit...\n");
    getchar();

    // Clean up
    fprintf(global_output, "unset multiplot\n");
    fclose(global_output);

    return 0;
}*/



static double x, y;
static double direction;
static int pendown;

static void
tortoise_reset ()
{
  x = y = 0.0;
  direction = 0.0;
  pendown = 1;

  fprintf(global_output, "clear\n");
  fflush(global_output);
}

static void
tortoise_pendown ()
{
  pendown = 1;
}

static void
tortoise_penup ()
{
  pendown = 0;
}

static void
tortoise_turn (double degrees)
{
  direction += M_PI / 180.0 * degrees;
}

static void
tortoise_move (double length)
{
  double newX, newY;

  newX = x + length * cos(direction);
  newY = y + length * sin(direction);

  if (pendown)
    draw_line(global_output, x, y, newX, newY);

  x = newX;
  y = newY;
}

int main (int argc, char* argv[])
{
  global_output = start_gnuplot ();

  tortoise_reset ();  // Initialize tortoise at (0, 0)

  // Draw a square
  tortoise_pendown ();
  for (int i = 1; i <= 4; ++i)
  {
    tortoise_move(3.0);
    tortoise_turn(90.0);
  }

  return EXIT_SUCCESS;
}
*/

