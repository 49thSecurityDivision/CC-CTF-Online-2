#include <stdio.h>
#include <string.h>
#include <unistd.h>

char *cat_string = "/usr/bin/cat";
char *echo_string = "/usr/bin/echo";
char *flag_string = "flag.txt";

void interesting_function(char *arg1, char *arg2) {
  char *args[] = { arg1, arg2, NULL };
  execv(args[0], args);

  return;
}

int check_pass(char *buff) {
  if(strcmp(buff, "niceTryToughGuy"))
  {
    printf ("\nWrong Password \n");
  }
  else
  {
    printf ("\nCorrect Password \n");
    return 1;
  }

  return 0;
}

int main(void)
{
  char buff[32];
  int pass = 0;

  printf("\nEnter something, tough guy:\n");

  gets(buff);

  pass = check_pass(buff);

  if(pass)
  {
    printf("\nCongrats! You get nothing!\n");
  }

  return 0;
}
