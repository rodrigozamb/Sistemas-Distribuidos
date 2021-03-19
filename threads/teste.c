#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int thread_count;

void* hello(void* rank) {
    long my_rank = (long) rank;
    printf("Hello from thread %ld of %d\n", my_rank, thread_count);
    return NULL;
}

int main(int argc, char* argv[]) {
    long thread;
    pthread_t* thread_handles;

    if(argc < 2) {
        printf("usage: %s <number of threads>", argv[0]); 
        return 1;
    }

    thread_count = strtol(argv[1], NULL, 10);
    thread_handles = malloc(thread_count*sizeof(pthread_t));

    for (thread = 0; thread < thread_count; thread++)
        pthread_create(&thread_handles[thread], NULL, hello, (void*) thread);

    printf("Hello from the main thread\n");
}