//银行一年整存零取的月息为0.63%
//有人打算存下一笔钱，使今后的五年，每年年底都可以取出1000元，且正好取完
//应该存入多少钱

#include <stdio.h>
int main()
{
	double a = 0.0063;	//月息
	double money = 0;	//第五年年底银行中还剩的钱
	for (int i = 0; i < 5; i++)	//前一年年底银行种剩余的钱
		money = (money + 1000) / (1 + a * 12);
	printf("%lf", money);
	return 0;
}