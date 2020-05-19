#include <stdio.h>
#include <string.h>

void function(char *name)
{
    char buffer[100];
    strcpy(buffer, name);
}

int main(int argc, char *argv[])
{
    function(argv[1]);
    return 0;
}

