#include<iostream>

using namespace std;

class array{
  
  int   *ptr;
  int   size;
  
  public:
    array(){
        
        ptr = NULL;
        size = 0;
        
        cout<<endl<<"Default"<<endl;
    }
    
    array(int   s){
        
        ptr = new int[s];
        size = s;
                cout<<endl<<"Parameterized"<<endl;
    }
    
    array(const array &co){
        
        ptr = new int[co.size];
        size = co.size;
        
        for(int i = 0; i < co.size; i++){
            
            *(ptr+i) = *(co.ptr + i);
            
        }
        
            cout<<endl<<"Copy COns"<<endl;
        
    }
    
    ~array(){
        
        cout<<"Gone"<<endl;
    }
    
    void    print(){
        cout<<endl;
        cout<<"ptr address: "<< ptr<<endl;
        
        for(int i = 0; i < size; i++){
            
            cout<<"\t"<<*(ptr+i);
        }
        cout<<endl;
    }
    
    void    put(){
        
        
        for(int i = 0; i < size; i++){
            
            *(ptr + i) = i + 30;
            
        }
        
    }
    
    
    void operator=(const array &co){
        
        cout<<endl<<"="<<endl;
        for(int i= 0; i<co.size; i++){
            
            *(this->ptr+i) = *(co.ptr+i);
            
        }
        //return (this);
        
    }
    
};



int main(){
    
    array A(10);
    
    A.print();
    A.put();
    A.print();
    
    array   C = A;
    
    A.put();
    
    array   B(A);
    C.print();    
    C = B;
    C.print();
    
    B.print();
    
    return  0;
}