//四位数字的车牌号，前两位相同，后两位相同
//四个数字不全相同，且该四位数为一个整数的平方

#include <stdio.h>
int main()
{
	int a, b;
	for (a = 31; a < 100; a++)
	{
		b = a * a;
		if (b / 1000 == b % 1000 / 100 && b % 100 / 10 == b % 10 && b / 1000 != b % 10)
			printf("%d", b);
	}
	return 0;
}