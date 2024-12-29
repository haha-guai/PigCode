//��1990��1��1���������������ɹ��
//������ں�����һ���Ǵ��㻹��ɹ��

#include <stdio.h>

//�ж��Ƿ�Ϊ����
int is_run(int year)
{
    if (year % 4 == 0 && year % 100 != 100 || year % 400 == 0)
        return 1;
    else
        return 0;
}

int main()
{
    int year, month, day;
    int i, sum = 0;
    printf("�����������ꡢ�¡���\n");
    scanf_s("%d%d%d", &year, &month, &day);

    //����������£����·�����
    int month_day[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    //���������������
    for (i = 1990; i < year; i++)
    {
        if (is_run(i))
            sum += 366;
        else
            sum += 365;
    }

    if (is_run(year))       //�������һ���·�����
        month_day[1] += 1;

    for (i = 0; i < month - 1; i++)     //���������������·�
        sum += month_day[i];

    sum += day;     //����ʣ��������������

    if (sum % 5 == 0 || sum % 5 == 4)
        printf("������ɹ��");
    else
        printf("�����Ǵ���");

    return 0;
}