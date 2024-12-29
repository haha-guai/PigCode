//方程ax^3 + bx^2 + cx + d = 0
//用牛顿迭代法求1附近的一个实根
//x = x0 - f(x0)/f`(x0)
//设迭代到|x - x0| <= 10e-5时结束

#include <stdio.h>
#include <math.h>

//单次牛顿迭代实现
double function(double a[4], double x0)
{
	double x;
	double fx0 = a[0] * pow(x0, 3) + a[1] * pow(x0, 2) + a[2] * x0 + a[3];	//方程
	double fx0_ = 3*a[0]*pow(x0, 2) + 2*a[1]*x0 + a[2];		//导数方程
	x = x0 - fx0 / fx0_;
	return x;
}

int main()
{
	double num[4], x0, x;
	int i;
	printf("ax^3 + bx^2 + cx + d = 0\n输入a、b、c、d的值：\n");
	for (i = 0; i <= 3; i++)
		scanf("%lf", &num[i]);
	printf("\n输入x0的值：\n");	//实际输入为x的值
	scanf("%lf", &x);
	do
	{
		x0 = x;					//将x的值赋给x0
		x = function(num, x0);
	} while (fabs(x - x0) > 1e-5);	//精度检验
	printf("%lf", x0);
	return 0;
}