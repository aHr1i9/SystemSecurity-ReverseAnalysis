#include <stdio.h>

int sub_num(int a, int b) {
    int s;
    s = a + b;
    printf("����������: %d\n",s);
    return s;
}

int main() {
    int i,m,n;
    int result=0;

    scanf("%d %d",&m,&n);
    printf("���������Ϊ:%d %d",m,n);

    //�������
    if (m>10) {
        printf("���ִ���10\n");
    }
    else {
        printf("����С�ڵ���10\n");
    }

    //ѭ�����
    for (i=0; i<=10; i++) {
        result += i;
        i++;
    }
    printf("1 + 2 + ... + 10 = %d\n",result);
    
    //����
    result = result + sub_num(m,n);
    printf("����������: %d\n",result);
    return 0;
}