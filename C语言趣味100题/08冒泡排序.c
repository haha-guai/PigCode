//冒泡排序
//对键盘输入的N个数字进行升序排列

#include <stdio.h>

#define N 5	//定义要排列的个数

int main()
{
	int i, j, k;
	int num_list[N];

	for (i = 0; i < N; i++)	//输入需要排列的数字
		scanf("%d", &num_list[i]);

	for (i = 0; i < N -1; i++)	//冒泡排序
		for (j = 0; j < N -1; j++)
			if (num_list[j] > num_list[j + 1])
			{
				k = num_list[j];
				num_list[j] = num_list[j + 1];
				num_list[j + 1] = k;
			}

	for (i = 0; i < N; i++)
		printf("%d\n", num_list[i]);
	return 0;
}