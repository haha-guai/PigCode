//��N�������������зŽ����飬���ö��ַ���������m�������е�λ��
//��m���ڣ����ӡ���±꣬��m���������ӡ"δ�ҵ�"

#include <stdio.h>

#define N 10	//���鳤��

int main()
{
	int num[N];
	int m, i;
	int high, low, flag = -1;

	scanf("%d", &m);

	for (i = 0; i < N; i++)		//����һ��ʾ������
		num[i] = 3 * i;

	high = N - 1;
	low = 0;

	while (low <= high)		//��m��С��������ʱ��i�ᳯһ�����򲻶��ƶ������low�����high
	{
		i = (high + low) / 2;	//iȡ�����м�
		if (num[i] == m)
		{
			flag = i;	//��m��С�����鷶Χ�ڣ���������û��mʱ�����lowҲ�����high��ֹͣѭ��
			break;
		}
		else if (num[i] > m)
			high = i - 1;
		else
			low = i + 1;
	}

	if (flag >= 0)	//����Ϊl>h��ֹͣѭ����f����
		printf("%d", i);
	else
		printf("û�ҵ�");
	return 0;
}