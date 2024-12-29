//小明有5本书，借给A、B、C三个人
//每人只借1本，共有多少种借法

#include <stdio.h>
int main()
{
    int a, b, c;
    int count = 0;
    for (a = 0; a < 5; a++)
        for (b = 0; b < 5; b++)
            for (c = 0; c < 5 && a != b; c++)   
                if (b != c && a != c)
                {
                    count += 1;
                    printf("A:%d,B:%d,C:%d      ", a, b, c);
                    if (count % 4 == 0)
                        printf("\n");
                }
     printf("共有%d种方法", count);
     return 0;
}