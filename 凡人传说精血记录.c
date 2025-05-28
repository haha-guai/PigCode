#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct{
    char name[20];
    int num;
    int type;
}Blood;

typedef struct{
    Blood list[100];
    int num;
}Blist;

void initBlist(Blist *bl);
void insertBlood(Blist *bl);
void checkBlood(Blist *bl);
void listBlood(Blist *bl);
void option(Blist *bl, int *flag);
void writeData(Blist *bl, char *name);
int readData(Blist *bl, char *name);

char fileName[] = "short_time/Pig.bin";

void main(){
    system("chcp 65001");
    Blist blist;
    Blist *bl = &blist;
    int dataFlag = readData(bl, fileName);
    if (dataFlag){
        initBlist(bl);
        printf("初始化成功\n");
    }
    int runFlag = 1;
    while(runFlag){
        option(bl, &runFlag);
    }
    
}

void initBlist(Blist *bl){
    bl->num = 0;
}

void insertBlood(Blist *bl){
    char name[20];
    int num, type;
    printf("输入精血名称:");
    scanf("%s", name);
    printf("输入精血品质:");
    scanf("%d", &type);
    printf("输入数量:");
    scanf("%d", &num);
    Blood blood;
    strcpy(blood.name, name);
    blood.num = num;
    blood.type = type;
    for (int i = 0; i < bl->num; i++)
        if (!strcmp(bl->list[i].name, name) && bl->list[i].type == type){
            bl->list[i].num += num;
            printf("精血已拥有%d\n", bl->list[i].num);
            return;
        }
    bl->list[bl->num++] = blood;
    printf("ok\n\n");
}

void checkBlood(Blist *bl){
    char bloodName[100][20];
    int bloodNum = 0;
    int bloodType[100][3] = {0};
    
    for (int i = 0; i < bl->num; i++){
        int vistied = 0;
        for (int j = 0; j < bloodNum; j++)
            if (!strcmp(bl->list[i].name, bloodName[j])){
                vistied = 1;
                bloodType[j][bl->list[i].type] += bl->list[i].num;
                break;
            }
        if (!vistied){
            strcpy(bloodName[bloodNum], bl->list[i].name);
            bloodType[bloodNum++][bl->list[i].type] += bl->list[i].num;
        }
    }
    for (int i = 0; i < bloodNum; i++){
        int a = bloodType[i][0];
        int b = bloodType[i][1];
        int c = bloodType[i][2];

        if ((c >= 2) && (((c - 2) / 3 + b) >= 2) && ((a + (b - 2 + (c - 2) / 3) / 3) >= 2)) printf("%s", bloodName[i]);
    }
    printf("\n");
}

void listBlood(Blist *bl){
    printf("精血列表：\n");
    printf("名称\t数量\t品质\n");
    for (int i = 0; i < bl->num; i++){
        char typename[7];
        switch (bl->list[i].type){
            case 0: strcpy(typename, "地品"); break;
            case 1: strcpy(typename, "玄品"); break;
            case 2: strcpy(typename, "黄品"); break;
        }
        printf("%s\t\t%d\t%s\n", bl->list[i].name, bl->list[i].num, typename);
    }
}
void option(Blist *bl, int *flag){
    int i;
    printf("输入你的操作(0:放入精血 1:天品精血 2:精血列表 3:清空屏幕 4:退出 5:测试退出)\n");
    scanf("%d", &i);
    switch (i){
        case 0:
            insertBlood(bl); break;
        case 1:
            checkBlood(bl); break;
        case 2:
            listBlood(bl); break;
        case 3:
            system("cls"); break;
        case 4:
            writeData(bl, fileName); *flag = 0; break;
        case 5:
            *flag = 0; printf("直接退出\n"); break;
    }
}

void writeData(Blist *bl, char *name){
    FILE *f = fopen(name, "wb");
    if (f == NULL) exit(1);
    fwrite(bl, sizeof(*bl), 1, f);
    printf("数据保存完成\n");
}

int readData(Blist *bl, char *name){
    FILE *f = fopen(name, "rb");
    if (f == NULL) return 1;
    fread(bl, sizeof(*bl), 1, f);
    printf("文件读取成功\n");
    return 0;
}