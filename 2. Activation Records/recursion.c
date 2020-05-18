#include<stdio.h>
int nthFib(int n){
	if(n == 0){
		return 0;
	}
	if(n == 1){
		return 1;
	}
	return (nthFib(n - 1) + nthFib(n - 2)); 
}
int main(){
	nthFib(3);
	return 0;
}
