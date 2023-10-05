#include <iostream>
using namespace std;

int dobavlenie_v_konec(int x[], int y[], int &c, int d) {
    for (int i = 0; i < d; i++) { 
        x[c++] = y[i]; // Я бы мог использовать insert() как и append в питоне но подумал что будет легко поэтому просто расписал код без сторонних функции
    }
    return 0;
}

int main()
{
    int c;
    int d;
    int a[1000];
    int b[1000];
    cout<<"Введи размер массива а ";
    cin>>c;
    
    cout<<"Введи размер массива b ";
    cin>>d;
    
    for(int i = 0;  i <= c - 1 ; i++){
        cout<<"Введите "<<i<< " элемент массива а: ";
        cin>>a[i]; 
    }
    
    for(int i = 0;  i <= d - 1 ; i++){
        cout<<"Введите "<<i<< " элемент массива b: ";
        cin>>b[i]; 
    }
    
    dobavlenie_v_konec(a,b,c,d);
    
    for(int i = 0; i < c; i++){
        cout<<a[i]<<" ";
    }
    
    
    return 0;
}