#include <iostream>

using namespace std;

int main()
{
    
    int m;
    int n;
    
    
    cout<<"Введи сколько элементов в массиве a ";
    cin>>m;
    cout<<"Введи сколько элементов в массиве b ";
    cin>>n;
    
    int*a = new int[m];
    int*b = new int[n];
    
    
    
    for(int i = 0; i < m; i++){
        cout<<"Введите "<<i+1<<" й элемент массива a = ";
        cin >> a[i];
    }
    
    for(int i = 0; i < n; i++){
        cout<<"Введите "<<i+1<<" й элемент массива b = ";
        cin >> b[i];
    }
    int*c = new int[m];
    int x = 0;

    
    for(int i = 0; i < m; ++i){
        for(int j = 0; j < n; ++j)
        if(a[i] == b[j]){
        c[x] = b[j];
        x++;
        break;
    }
    }
    if(x == 0){
        cout<<"Общий элемент жок";
    }
    else{
    for(int i = 0; i < x; ++i){
        cout<<c[i]<<" ";
    }
    }
    
    
    return 0;
}