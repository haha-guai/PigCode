//计算个人所得税，输入金额，输出应缴纳金额
/*
起征点为3500
不超过1500部分，3%
1500~4500部分，10%
4500~9000部分，20%
9000~35000部分，25%
35000~55000部分，30%
55000~80000部分，35%
超过80000部分，45%
*/

#include<stdio.h>
int main()
{
	double earnings;
	double submit_money;
	scanf("%lf", &earnings);
	if (earnings - 3500 > 80000)
		submit_money = (earnings - 80000 - 3500) * 0.45 + 25000 * 0.35 + 20000 * 0.3 + 24000 * 0.25 + 4500 * 0.20 + 3000 * 10 + 1500 * 0.03;
	else if (earnings - 3500 > 55000)
		submit_money = (80000 - earnings) * 0.35 + 20000 * 0.3 + 24000 * 0.25 + 4500 * 0.20 + 3000 * 10 + 1500 * 0.03;
	else if (earnings - 3500 > 35000)
		submit_money = (55000 - earnings) * 0.3 + 24000 * 0.25 + 4500 * 0.20 + 3000 * 10 + 1500 * 0.03;
	else if (earnings - 3500 > 9000)
		submit_money = (35000 - earnings) * 0.25 + 4500 * 0.20 + 3000 * 10 + 1500 * 0.03;
	else if (earnings - 3500 > 4500)
		submit_money = (9000 - earnings) * 0.20 + 3000 * 10 + 1500 * 0.03;
	else if (earnings - 3500 > 1500)
		submit_money = (4500 - earnings) * 0.10 + 1500 * 0.03;
	else if (earnings - 3500 > 0)
		submit_money = (earnings - 3500) * 0.03;
	else
		submit_money = earnings;
	printf("\n%.2lf", submit_money);
	return 0;
}