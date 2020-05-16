#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
pthread_mutex_t lock;
//seconds is the shared resource between seconds and minutes
//minutes is the shared resource between minutes and hours
//sync between seconds and minute at 00:00:59
//sync between the three counters at the instance 00:59:59
typedef struct myclock{
	int hours;
	int minutes;
	int seconds;
} myclock;
myclock c1 = {0, 0, 0};
void* secondCount(void* status){
	while((*(char*)status) != '\n'){
		sleep(1);
		//pthread_mutex_lock(&lock);	//output console is the shared resource
		(c1.seconds)++;
		//pthread_mutex_unlock(&lock);
	}
}
void* minuteCount(void* status){ 
	while((*(char*)status) != '\n'){
		if(c1.seconds == 60){
			(c1.minutes)++;
			c1.seconds %= 60;
		}
	}
}
void* hourCount(void* status){
	while((*(char*)status) != '\n'){
		if(c1.minutes == 2){
			(c1.hours)++;
			c1.minutes %= 2;
		}
	}
}
void* printClock(){
	while(1){
		sleep(1);
		printf("%d:%d:%d\n", c1.hours, c1.minutes, c1.seconds);
	}
}
int main(){
	char status = '\0';
	int state;
	pthread_t id1, id2, id3, id4;
	if (pthread_mutex_init(&lock, NULL) != 0) { 
        printf("\n mutex init has failed\n"); 
        exit(1); 
    	}
	printf("Starting Threads (Press Enter to terminate)\n");
	state = pthread_create(&id1, NULL, secondCount, &status);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	state = pthread_create(&id2, NULL, minuteCount, &status);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	state = pthread_create(&id3, NULL, hourCount, &status);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	state = pthread_create(&id4, NULL, printClock, NULL);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	scanf("%c", &status);
	pthread_join(secondCount, NULL);
	pthread_join(minuteCount, NULL);
	pthread_join(hourCount, NULL);
	pthread_join(printClock, NULL);
	printf("Out of The Threads\n");
	pthread_mutex_destroy(&lock); 
	return 0;
}

