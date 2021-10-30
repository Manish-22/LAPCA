//less efficient method using swap

void insertNode(int my_heap[], int n, int key){
    int child_ind = n+1;
    int parent_ind;
    int temp;
    my_heap[child_ind] = key;
    parent_ind =  child_ind/2;
    while(child_ind > 1 && my_heap[parent_ind] < key){
        temp = my_heap[child_ind]; //swap
        my_heap[child_ind] = my_heap[parent_ind];
        my_heap[parent_ind] = temp;
        child_ind = parent_ind;
        parent_ind = parent_ind/2;
    }
}

void printArray(int my_heap[], int n){
    int i;
    for(i=1; i<=n; i++){
        printf("%d ", my_heap[i]);
    }
    printf("\n");
}


int main() 
{ 
    
    int arr_len = 7;
    int arr[] = { 10, 2, 3, 5, 4, 8, 15};  
    int my_heap[100]; //1-indexed
    int n = 0;
    int i;
  
    for(i = 0; i<arr_len; i++){
        insertNode(my_heap, n, arr[i]); 
        n++;
        printArray(my_heap, n); 
    }
  
    //printArray(my_heap, n); 
    // Final Heap will be: 
    // 15 
    //    /   \ 
    // 5     10 
    //  / \   / \
    // 2   4 3   8
    return 0; 
} 
