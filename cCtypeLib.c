
#include <stdio.h>
#ifdef __cplusplus
extern "C" {
#endif

typedef struct A
{
  unsigned char* a1;
  int a2;
} A;

typedef void (*python_cb_t)(A *myStruct);
int testCB(python_cb_t cb,int myInt);


int testCB(python_cb_t cb,int myInt) {
  A myStruct;

  myStruct.a1 = "Cows Rule!";
  myStruct.a2 = myInt;

  fprintf(stderr,"C:testCB cb = 0x%x  \n",(unsigned int) cb);
  

  (cb)(&myStruct);

  return 0;

}



#ifdef __cplusplus
};
#endif
