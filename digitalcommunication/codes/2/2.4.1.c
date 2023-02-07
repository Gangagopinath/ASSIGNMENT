
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {



// open the file to write the data
FILE *fp;
double u1,u2,t;
fp = fopen("tri.dat", "w");



// generate 1000000 random samples of T = U1 + U2
for (int i = 0; i < 1000000; i++) {
     u1 = (double) rand() / RAND_MAX;
     u2 = (double) rand() / RAND_MAX;
     t = u1 + u2;
    fprintf(fp, "%lf\n", t);
}

// close the file
fclose(fp);

return 0;
}



