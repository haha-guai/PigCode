//ð������
//�Լ��������N�����ֽ�����������

#include <stdio.h>

#define N 5	//����Ҫ���еĸ���

int main()
{
	int i, j, k;
	int num_list[N];

	for (i = 0; i < N; i++)	//������Ҫ���е�����
		scanf("%d", &num_list[i]);

	for (i = 0; i < N -1; i++)	//ð������
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