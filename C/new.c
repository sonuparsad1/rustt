#include <stdio.h>
int main(){
    int a,b;
    printf('enter a and b');
    scanf("%d","%d",&a,&b);
    int temp =a;
    a=b;
    b = temp;
    printf("%d %d",a,b);
    return 0;
}