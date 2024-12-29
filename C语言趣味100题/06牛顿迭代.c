//����ax^3 + bx^2 + cx + d = 0
//��ţ�ٵ�������1������һ��ʵ��
//x = x0 - f(x0)/f`(x0)
//�������|x - x0| <= 10e-5ʱ����

#include <stdio.h>
#include <math.h>

//����ţ�ٵ���ʵ��
double function(double a[4], double x0)
{
	double x;
	double fx0 = a[0] * pow(x0, 3) + a[1] * pow(x0, 2) + a[2] * x0 + a[3];	//����
	double fx0_ = 3*a[0]*pow(x0, 2) + 2*a[1]*x0 + a[2];		//��������
	x = x0 - fx0 / fx0_;
	return x;
}

int main()
{
	double num[4], x0, x;
	int i;
	printf("ax^3 + bx^2 + cx + d = 0\n����a��b��c��d��ֵ��\n");
	for (i = 0; i <= 3; i++)
		scanf("%lf", &num[i]);
	printf("\n����x0��ֵ��\n");	//ʵ������Ϊx��ֵ
	scanf("%lf", &x);
	do
	{
		x0 = x;					//��x��ֵ����x0
		x = function(num, x0);
	} while (fabs(x - x0) > 1e-5);	//���ȼ���
	printf("%lf", x0);
	return 0;
}