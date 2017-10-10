#include <bits/stdc++.h>

using namespace std;

float c=0.01,x[1000], y[1000],dy, weight_x, weight_y,weight_bias,bias=1.0,desired_result[1000],
guess_result[1000],error[1000],nweight_x,nweight_y,nweight_bias,fresult[1000];
int i , j, k ;
int doutput(int x, int y, int i)
{
    dy=2*x+1;
    if(dy<y)
        return(1);
    if(dy>y)
        return(-1);
    else
        return(0);
}
int goutput(int i)
{
    float sum;
    sum=x[i]*weight_x+y[i]*weight_y+1*weight_bias;
    if(sum>0)
        return(1);
    else
        return(-1);
}
int goutput_i(int x, int y)
{
    float sum;
    sum=x*weight_x+y*weight_y+1*weight_bias;
    if(sum>0)
        return(1);
    else
        if(sum<0)
            return(-1);
        else
            return(0);
}
int main(){
int c1=0,c2=0,x1,y1;
for(i=0;i<1000;i++){
    x[i]=(rand()%100);
    y[i]=(rand()%100);
}
    weight_x=((rand()%200)-99)/100.0;
    weight_y=((rand()%200)-99)/100.0;
    weight_bias=((rand()%200)-99)/100.0;

/*-------------------------trainer----------------------------*/
    for(i=0;i<1000;i++)
    {
        desired_result[i]=doutput(x[i],y[i],i);

        guess_result[i]=goutput(i);
        error[i]=desired_result[i]-guess_result[i];

        weight_x=weight_x+error[i]*x[i]*c;
        weight_y=weight_y+error[i]*y[i]*c;
        weight_bias=weight_bias+error[i]*c;
    }
    cout<<"Enter x coordinate of the point: ";
    cin>>x1;
    cout<<"Enter y coordinate of the point: ";
    cin>>y1;
    c1=goutput_i(x1,y1);
    if(c1==1)
        cout<<"Point is Above the line";
    else
        cout<<"Point is Below the line";

}

