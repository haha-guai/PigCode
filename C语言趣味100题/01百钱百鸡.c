//公鸡元5只，母鸡3元1只，小鸡3只1元
//用100元买100只鸡，有哪些买法？

#include <stdio.h>
int main()
{
    int cock, hen, chick;
    for (cock = 0; cock <= 20; cock++)
        for (hen = 0; hen <= 33; hen ++)
        {
            chick = 100 - cock - hen;
            if (5*cock + 3*hen + chick * 1.0/3 == 100)
                printf("公鸡：%2d，母鸡：%2d，小鸡：%2d\n", cock, hen, chick);
        }
    return 0;
}