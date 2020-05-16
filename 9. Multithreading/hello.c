//Threaded program to print Hello repeatedly until user presses enter
#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
void* proc(void* status){
	while(*((char*)status) != '\n'){
		printf("Hello\n");
		sleep(1);
	}
}
int main(){
	pthread_t id;
	char status = '\0';
	int state;
	printf("Starting Hello Thread (Press Enter to terminate)\n");
	state = pthread_create(&id, NULL, proc, &status);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	scanf("%c", &status);
	pthread_join(id, NULL);
	printf("Out of Hello Thread\n");
	return 0;
}
