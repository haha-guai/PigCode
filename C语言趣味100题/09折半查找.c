//将N个有序整数数列放进数组，利用二分法查找整数m在数列中的位置
//若m存在，则打印其下标，若m不存在则打印"未找到"

#include <stdio.h>

#define N 10	//数组长度

int main()
{
	int num[N];
	int m, i;
	int high, low, flag = -1;

	scanf("%d", &m);

	for (i = 0; i < N; i++)		//生成一个示例数组
		num[i] = 3 * i;

	high = N - 1;
	low = 0;

	while (low <= high)		//当m大小超出数组时，i会朝一个方向不断移动，最后low会大于high
	{
		i = (high + low) / 2;	//i取两点中间
		if (num[i] == m)
		{
			flag = i;	//当m大小在数组范围内，但数组中没有m时，最后low也会大于high，停止循环
			break;
		}
		else if (num[i] > m)
			high = i - 1;
		else
			low = i + 1;
	}

	if (flag >= 0)	//当因为l>h而停止循环后，f不变
		printf("%d", i);
	else
		printf("没找到");
	return 0;
}