#define CRT_NO_SECURE_WARNINGS
#include <stdio.h>
#include <stdlib.h>


int main(void) {
	int a;
	int i;
	scanf("%d", &a);
	for (i = 0; i < a; i++) {
		int x,y;
		scanf("%d %d", &x, &y);
		printf("Case #%d: %d\n", i+1, x + y);
	}
	return 0;
}