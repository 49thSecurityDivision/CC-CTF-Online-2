#include <stdio.h>


char *flag0 = "flag{KqU";
char *flag1 = "3tIdk5QU";
char *flag2 = "josbolCh";
char *flag3 = "whE0YfEw";
char *flag4 = "UD9y3}";

int main(void) {
  if (flag0 == flag1) {
    printf("Match!");
  }

  if (flag1 == flag2) {
    printf("Match!");
  }

  if (flag2 == flag3) {
    printf("Match!");
  }

  if (flag3 == flag4) {
    printf("Match!");
  }

  if (flag4 == flag0) {
    printf("Match!");
  }

  return 0;
}
