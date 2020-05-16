#include<stdio.h>
void message(void){
	printf("Hello World!");
}
int overflow(void){
	int a[5];
	int i = 0;
	for(i = 0; i < 25; i++){
		a[i] = 2;
	}
	return 0;
}
int main(){
	int i = overflow();
	return 0;
}

