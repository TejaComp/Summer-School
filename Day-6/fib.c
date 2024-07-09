int fib(int n){
int prev=0;
int curr=1;
int next;
for (int i=0;i<n;i++){
next=prev +curr;
prev=curr;
curr=next;
}
return curr;
}