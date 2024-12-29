//从1990年1月1日起三天打鱼两天晒网
//求该日期后任意一天是大鱼还是晒网

#include <stdio.h>

//判断是否为闰年
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
    printf("请依次输入年、月、日\n");
    scanf_s("%d%d%d", &year, &month, &day);

    //非闰年情况下，各月份天数
    int month_day[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    //所有完整年的天数
    for (i = 1990; i < year; i++)
    {
        if (is_run(i))
            sum += 366;
        else
            sum += 365;
    }

    if (is_run(year))       //完善最后一年月份天数
        month_day[1] += 1;

    for (i = 0; i < month - 1; i++)     //多出来的年的完整月份
        sum += month_day[i];

    sum += day;     //加上剩余天数，总天数

    if (sum % 5 == 0 || sum % 5 == 4)
        printf("这天是晒网");
    else
        printf("这天是打鱼");

    return 0;
}