#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
pthread_spinlock_t lock1, lock2;
//seconds is the shared resource between seconds and minutes controlled by lock1
//minutes is the shared resource between minutes and hours controlled by lock2
//sync between seconds and minute at 00:00:59
//sync between the three counters at the instance 00:59:59
typedef struct myclock{
	int hours;
	int minutes;
	int seconds;
} myclock;
myclock c1 = {0, 0, 0};
void* secondCount(void* status){
	while(1){
		sleep(1);
		pthread_spin_lock(&lock1);
		(c1.seconds)++;
		pthread_spin_unlock(&lock1);
	}
}
void* minuteCount(void* status){ 
	while(1){
		if(c1.seconds == 60){
			pthread_spin_lock(&lock1);
			c1.seconds %= 60;
			pthread_spin_unlock(&lock1);
			pthread_spin_lock(&lock2);
			(c1.minutes)++;
			pthread_spin_unlock(&lock2);
		}
	}
}
void* hourCount(void* status){
	while(1){
		if(c1.minutes == 60){
			pthread_spin_lock(&lock2);
			c1.minutes %= 60;
			pthread_spin_unlock(&lock2);
			(c1.hours)++;
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
	int state;
	pthread_t id1, id2, id3, id4;
	if (pthread_spin_init(&lock1, PTHREAD_PROCESS_SHARED) != 0) { 
        printf("\n Spinlock init has failed\n"); 
        exit(1); 
    	}
    	if (pthread_spin_init(&lock2, PTHREAD_PROCESS_SHARED) != 0) { 
        printf("\n Spinlock init has failed\n"); 
        exit(1); 
    	}
	printf("Starting Threads (Press Ctrl+C to terminate)\n");
	state = pthread_create(&id1, NULL, secondCount, NULL);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	state = pthread_create(&id2, NULL, minuteCount, NULL);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	state = pthread_create(&id3, NULL, hourCount, NULL);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	state = pthread_create(&id4, NULL, printClock, NULL);
	if(state != 0){
		printf("Could not create thread, exiting.\n");
		exit(1);
	}
	pthread_join(id1, NULL);
	pthread_join(id2, NULL);
	pthread_join(id3, NULL);
	pthread_join(id4, NULL);
	printf("Out of The Threads\n");
	pthread_spin_destroy(&lock1);
	pthread_spin_destroy(&lock2);
	return 0;
}

