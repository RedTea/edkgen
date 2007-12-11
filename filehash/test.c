#include "test.h"

int main(){
    uchar o1[16],o2[32];
    //f = fopen("md4.py", "rb");
    CreateMD4FromInput(NULL,"",0,o1);
    Encode(o2,o1);
    printf("%s\n",o2);
    printf("sizeof(short)%d\n",sizeof(short));
    printf("sizeof(int)%d\n",sizeof(int));
    printf("sizeof(long)%d\n",sizeof(long));
}
