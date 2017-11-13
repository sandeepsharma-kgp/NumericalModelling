#include <bits/stdc++.h>
using  namespace std;
#define PI 3.14159265
int main()
{
	float xc,yc;
	int n;
	cout << "Enter the centres" <<endl;
	cin>>xc>>yc;
	cout <<"Enter the number of segments"<<endl;
	cin>>n;
	float h=50;
	float ym=50;
	float beta;
	cout <<"Enter the slope angle"<<endl;
	cin>>beta;
	beta = beta*PI/180.0;
	float phi = 22.0*PI/180.0;
	float r = sqrt(yc*yc+xc*xc);
	float xm = xc + sqrt(r*r - pow(yc-ym,2));
	float delta_x = xm/n; 
	float hs[n];
	float w[n];
	float alpha[n];
	float gamma = 1500;
	for(int i=0;i<n;i++)
	{
		float xl = i*delta_x;
		float xr = (i+1)*delta_x;
		float x_mid = (xl+xr)/2.0;
		float y_mid = yc-sqrt(r*r - pow(x_mid-xc,2));
		if(xl<h/tan(beta))
			hs[i] = x_mid*tan(beta) -y_mid;
		else
			hs[i]= h-y_mid;
		alpha[i] = atan(-(x_mid-xc)/(y_mid-yc));
		w[i] = hs[i]*delta_x*gamma;
		cout<<w[i]<<" "<<alpha[i]<<" "<<hs[i]<<endl;
	}
	float FOS_old = 1.0;
	float FOS_new = 0.0;
	float error=2.0;
	while(fabs(error)>.0001)
	{
		float numerator=0;
		float denominator = 0;
		for(int i=0;i<n;i++)
		{
			numerator+=((7000+1500*hs[i]*tan(phi))*delta_x/cos(phi))/(1+(tan(alpha[i])*tan(phi))/FOS_old);
			denominator+= w[i]*sin(alpha[i]);
		}
		FOS_new = numerator/denominator;
		error = FOS_new-FOS_old;
		cout<<FOS_new<<endl;
		FOS_old = FOS_new;
	}
	cout << FOS_new<<endl;
}