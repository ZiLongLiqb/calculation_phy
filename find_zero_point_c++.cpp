//author------------lizilong--------------
//all rights reserved.
#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <iomanip>
#include <ctime>
using namespace std;
//import necessary library file.
//difine a function we need. 
double func(double x){
	return exp(x)*log(x)-x*x;
}

//the main body of the program.
//the parameter are the accuracy we need, two points which satisfy func(point_1)*func(point_2)<0.
void dichonomy(double accuracy, double point_1, double point_2,double (*func)(double)){
	//the parameter count is to count the cycles we need.
	static int count=0;
	double point_3=(point_1+point_2)/2;
	count+=1;
	if((point_2-point_1)/2<=accuracy){
		cout<<"The result is:"<<fixed<<setprecision(20)<<point_3<<endl;
		cout<<"It takes "<<count<<" times to get the result under the accuracy."<<endl;
		return;
	}
	if(func(point_3)==0){
		cout<<"The accurate result is"<<fixed<<setprecision(20)<<point_3<<endl;
		cout<<"It takes "<<count<<" times to get the result under the accuracy."<<endl;
		return;
	}
	else if(func(point_3)*func(point_2)<0){
		dichonomy(accuracy,point_3,point_2,func);
	}
	else{
		dichonomy(accuracy,point_1,point_3,func);
	}
}

//main function
int main(){
	clock_t start_time,end_time;
	start_time=clock();
	dichonomy(0.000001,1,2,func);
	end_time=clock();
	cout<<"The running time is "<<double(end_time-start_time)<<endl;
	return 0;
}