// get the height of the column '#' as input
// print the column '#' of height user inputed

#include <cs50.h>
#include <stdio.h>

void print_column(int height);

int main(void)
{
    int h = get_int("Height: ");
    print_column(h);
}

void print_column(int height)
{
    for (int i = 0; i < height; i++)
    {
        printf("#\n");
    }
}
