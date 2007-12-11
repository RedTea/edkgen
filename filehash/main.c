#include <stdio.h>
#include <stdlib.h>
#include "md4.h"
#include "ed2k.h"
#include <sys/stat.h>

long get_filesize(char *FileName)
{
    struct stat file;
    if(!stat(FileName,&file))return file.st_size;
    return 0;
}

int main(int argc, char *argv[])
{
    int i;
    uchar o1[16],o2[32];
    FILE *f;
    long size;

    if (argc > 1)
        for (i = 1; i < argc; i++)
            {
                f = fopen (argv[i], "rb");
                if(f!=NULL){
                    size = get_filesize(argv[i]);
                    //printf("%d\n",size);
                    //CreateMD4FromFile(f, size, o1);
                    CreateHashFromFile(f, size, o1);
                    Encode(o2,o1);
                    //cout<<o2<<endl;
                    printf("%s",o2);
                    fclose(f);
                }
                printf("\n");
            }
    //system("PAUSE");
    return EXIT_SUCCESS;
}
