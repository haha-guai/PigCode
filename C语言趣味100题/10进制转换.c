//给定一个M进制的数x，实现对x向任意非M进制数的转换

#include <stdio.h>

#define MAXCHAR 100	//数组最大长度

int char_to_num(char ch);	//字符转数字
char num_to_char(int num);	//数字转字符
long source_to_decimal(char temp[], int source);	//原进制转10进制
int decimal_to_other(char temp[], long decimal_num, int num_system);	//十进制转其他进制
void return_number(char temp[], int length);	//返回结果


int main()
{
	int source;	//原进制
	int num_system;	//新进制
	int length;
	long decimal_num;
	char temp[MAXCHAR];
	int flag = 1;
	while (flag)
	{
		printf("输入转换前的数：");
		scanf("%s", temp);
		printf("转换前的数制是：");
		scanf("%d", &source);
		printf("\n转换后的数制是：");
		scanf("%d", &num_system);
		printf("\n转换后的数是：\n");
		decimal_num = source_to_decimal(temp, source);
		length = decimal_to_other(temp, decimal_num, num_system);
		return_number(temp, length);
		printf("\n输入非0数字继续\n");
		scanf("%d", &flag);
	}

	return 0;
}

int char_to_num(char ch)//字符转数字，ASCII码
{
	if (ch >= '0' && ch <= '9')
		return ch - '0';
	else
		return ch - 'A' + 10;
}

char num_to_char(int num)//数字转字符
{
	if (num >= 0 && num <= 9)
		return (char)('0' + num);
	else
		return (char)('A' + num - 10);
}

long source_to_decimal(char temp[], int source)//其他进制转十进制
{
	long decimal_num = 0;
	int length;
	int i;
	for (i = 0; temp[i] != '\0'; i++)
		decimal_num = (decimal_num * source) + char_to_num(temp[i]);
	return decimal_num;
}

int decimal_to_other(char temp[], long decimal_num, int num_system)//十进制转其他进制
{
	int i = 0;
	while (decimal_num)
	{
		temp[i] = num_to_char(decimal_num % num_system);//最后得到的是逆序的该进制数 除R取余法
		decimal_num = decimal_num / num_system;
		i++;
	}
	temp[i] = '\0';
	return i;
}

void return_number(char temp[], int length)//逆序输出，得到实际数
{
	int i;
	for (i = length - 1; i >= 0; i--)//i-1为倒数第二个元素，即最后的数字
		printf("%c", temp[i]);
}