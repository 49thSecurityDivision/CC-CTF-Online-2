#include <stdio.h>
#include <string.h>
#include <unistd.h>

void interesting_function(void) {
  char *args[] = { "/usr/bin/cat", "flag.txt", NULL };
  execv(args[0], args);
}

int check_pass(char *buff) {
    if(strcmp(buff, "fuzzme"))
    {
        printf ("\n Wrong Password \n");
    }
    else
    {
        printf ("\n Correct Password \n");
        return 1;
    }

    return 0;
}

int main(void)
{
    char buff[15];
    int pass = 0;

    printf("\n Enter the password : \n");
    gets(buff);

    pass = check_pass(buff);

    if(pass)
    {
       /* Now Give root or admin rights to user*/
        printf ("\n Root privileges given to the user \n");
    }

    return 0;
}
