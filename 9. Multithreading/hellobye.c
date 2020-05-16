//Program to print hello and bye in a synchronised manner
#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
pthread_spinlock_t lock;
void* hello(void* status){ 
	while((*(char*)status) != '\n'){
		pthread_spin_lock(&lock);
		printf("Hello World\n");
		sleep(1);
		pthread_spin_unlock(&lock);
	}
}
void* bye(void* status){
	while((*(char*)status) != '\n'){
		pthread_spin_lock(&lock);
		printf("Goodbye World\n");
		sleep(1);
		pthread_spin_unlock(&lock);
	}
}
void* exitcheck(void* status){
	while((*(char*)status) != '\n'){
		scanf("%c", ((char*)status));
	}
}
int main(){
	char status = '\0';
	int state;
	pthread_t id1, id2, id3;
	if (pthread_spin_init(&lock, PTHREAD_PROCESS_SHARED) != 0) { 
        printf("\n Spinlock init has failed\n"); 
        exit(1); 
    	}
    	state = pthread_create(&id3, NULL, exitcheck, &status);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	printf("Starting Threads (Press Enter to terminate)\n");
	state = pthread_create(&id1, NULL, hello, &status);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	state = pthread_create(&id2, NULL, bye, &status);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	pthread_join(id1, NULL);
     pthread_join(id2, NULL);
	printf("Out of The Threads\n");
	pthread_spin_destroy(&lock); 
	return 0;
}

