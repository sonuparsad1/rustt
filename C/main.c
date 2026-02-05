#include <stdio.h>
void ab(int *arr, int length) {
    for(int i = 0; i < length; i++) {
        printf("%d ", *(arr+i));
    }
}
int main() {
    int arr[] = {1,2,3,4,5};
    int length = sizeof(arr) / sizeof(arr[0]);
    printf("%d \n",length);
    int *l = arr;
    int *r = arr +length -1;
    while (l<r){
        int temp = *l;
        *l = *r;
        *r = temp;
        l++;
        r--;
    }
    ab(arr,length);
}

