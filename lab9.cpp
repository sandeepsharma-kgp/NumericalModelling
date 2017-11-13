#include <bits/stdc++.h>
using namespace std;
#define PI 3.14159265
double influence(double r,double R)
{
    double result = 1/(R*R)*(exp(-PI*r*r/(R*R)));
    return result;
}
bool issafe(int i,int j,int k,int l,int m,int n,double R)
{
    double r = sqrt(pow((i-k)*10,2)+pow((j-l)*10,2));
    if(k<m && k>=0 && l<n && l>=0 && r<=R)
        return true;
    else
        return false;
}
int main()
{
    double l=500;
    double b=100;
    double d = 300;
    double alpha = (15*PI)/180;
    double R = d*tan(alpha);
    cout << R<<endl;
    int X= l+2*R;
    int Y = b+2*R;
    vector<vector<double>> grid(X/10,vector<double>(Y/10,0.0));
    for(int i=R/10;i<(l+R)/10;i++)
    {
        for(int j=R/10;j<(b+R)/10;j++)
            grid[i][j] = 1;
    }
    vector<vector<double>> subsidence(X/10,vector<double>(Y/10,0.0));
    for(int i=0;i<grid.size();i++)
    {
        for(int j=0;j<grid[0].size();j++)
        {
            subsidence[i][j]=0;
            for(int k=(i-R/10);k<=(i+R/10);k++)
            {
                for(int l=j-R/10;l<=j+R/10;l++)
                {
                    if(issafe(i,j,k,l,grid.size(),grid[0].size(),R))
                        subsidence[i][j]+=grid[k][l]*influence(sqrt(pow((i-k)*10,2)+pow((j-l)*10,2)),R);
                }
            }
        }
    }
    ofstream write;
    write.open("f.txt");
    for(int i=0;i<subsidence.size();i++)
    {
        for(int j=0;j<subsidence[0].size();j++)
            write<<subsidence[i][j]<<" ";
        write<<endl;
    }


    return 0;
}