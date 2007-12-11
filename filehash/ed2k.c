#include "ed2k.h"

void CreateHashFromFile(FILE *file, uint32 Length, uchar *Output) {
    uint32 togo = Length;
    uint16 hashcount = Length/PARTSIZE + 1;
    uchar hashlist[hashcount][16];
    uint16 i;
    uchar o1[16],o2[32];
    //uchar o[16];
    if(hashcount==1){
        CreateMD4FromFile(file, togo, Output);
        //printf("%s",o2);
    }
    else{
        for (i = 0; i < hashcount; i++) {
    		//uchar* newhash = new uchar[16];
    		if(togo>=PARTSIZE){
                CreateMD4FromFile(file, PARTSIZE, hashlist[i]);
                //Encode(o2,hashlist[i]);
                //printf("%s\n",o2);
            }else{
                CreateMD4FromFile(file, togo, hashlist[i]);
                //Encode(o2,hashlist[i]);
                //printf("%s\n",o2);
            }
    		togo -= PARTSIZE;
    		//Encode(o,hashlist[0]);
            //printf("%d\n",strlen(o));
        }
        CreateMD4FromString(hashlist, hashcount*16, Output);
    }
}
