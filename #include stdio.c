#include stdio.h

int add(int x, int y);
int sub(int x,int y);

int main()
{
    printf("%d + %d = %d/n", 4, 5, add(4,5));
    printf("%d - %d = %d/n", 7, 10, add(7, 10));

    return 0;
}

