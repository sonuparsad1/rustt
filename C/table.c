#include <stdio.h>
int main(){
    int t,f;
    printf("enter table to be printed: ");
    scanf("%d",&t);
    printf("enter how may times to be printed: ");
    scanf("%d",&f);
    int i;
    for(i=1;i<=f;i++){
        printf("%d x %d = %d \n",t,i,t*i);
    }


}