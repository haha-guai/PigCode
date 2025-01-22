/*
1-0.63%
2-0.66%
3-0.69%
5-0.75%
8-0.84%
2000元, 存20年，求最优方案
*/

#include <stdio.h>
#include <math.h>
int main()
{
	double result, max = 0;
	int x8, x5, x3, x2, x1;
	int y8, y5, y3, y2, y1;
	for (x8 = 0; x8 * 8 <= 20; x8++)
		for (x5 = 0; x8 * 8 + x5 * 5 <= 20; x5++)
			for (x3 = 0; x8 * 8 + x5 * 5 + x3 * 3 <= 20; x3++)
				for (x2 = 0;  x8 * 8 + x5 * 5 + x3 * 3 + x2 * 2 <= 20; x2++)
				{
					x1 = 20 - x8 * 8 - x5 * 5 - x3 * 3 - x2 * 2;
					result = 2000 * pow(1 + 0.0063 * 12, x1)
						* pow(1 + 0.0066 * 12 * 2, x2)
						* pow(1 + 0.0069 * 12 * 3, x3)
						* pow(1 + 0.0075 * 12 * 5, x5)
						* pow(1 + 0.0084 * 12 * 8, x8);
					if (result > max)
					{
						max = result;
						y8 = x8;
						y5 = x5;
						y3 = x3;
						y2 = x2;
						y1 = x1;
					}
				}
	printf("%0.2lf", max);
	printf("\n%d\n%d\n%d\n%d\n%d", y8, y5, y3, y2, y1);
	return 0;
}