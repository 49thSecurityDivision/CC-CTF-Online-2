#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>

// gcc ED206.c -m32 -no-pie -g -fno-stack-protector -z norelro -z execstack -o ED206

struct internet {
  int priority;
  char *name;
};

void winner() {
  char *args[] = { "/usr/bin/cat", "flag.txt", NULL };
  execv(args[0], args);
  //printf("XXXXXXXXXXXXX winner\n");
}

int main(int argc, char **argv) {
  struct internet *i1, *i2, *i3;
  char arg1[25];
  char arg2[25];

  //if ( argc != 3) {
  //  printf("Usage: %s string1 string2n", argv[0]);
  //  exit(0);
  //}
  printf("Enter a string argument:\n");
  fgets(arg1, sizeof(arg1), stdin);
  
  printf("Enter another string argument (maybe...):\n");
  fgets(arg2, sizeof(arg2), stdin);
  
  i1 = malloc(sizeof(struct internet));
  i1->priority = 1;
  i1->name = malloc(8);
  
  i2 = malloc(sizeof(struct internet));
  i2->priority = 2;
  i2->name = malloc(8);
  
  printf("Your 1st arg was: %s\n", arg1);
  printf("Your 2nd arg was: %s\n", arg2);
  strcpy(i1->name, arg1);
  strcpy(i2->name, arg2);
  
  printf("vr0n says 'hello!'\n");
  exit(0);
}
