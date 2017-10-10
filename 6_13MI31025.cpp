#include<bits/stdc++.h>
float g=9.81,hdash,r,Vs,Ts,Ta,uH,F,xf,s,dtdz,ans1,ans2,ans3,p,a,c,d,f,sigmay,sigmaz,effh,ubar,y,x=0.5,uH3;
float Q= 0.9315*pow(10,9)*((500)/0.45)/3600;
int cond1,cond2,cond3,atmcl,i;

float plumerise(int cond);
int findclass(int cond,float uH2);
float findexp(int atmclass);
void findvalues(int atmclass,float x);
float findconc(float x);
int main ()
{	//250,2,15,140,25,5,0.002,1,2,2.5,2
	printf("Enter the height of the stack(in mts)  : ");
	scanf("%f",&hdash);
	printf("Enter Stack inside radius(in mts)      : ");
	scanf("%f",&r);
	printf("Enter stack gas exit velocity(in m/s)  : ");
	scanf("%f",&Vs);
	printf("Enter stack temperature(in celsius)    : ");
	scanf("%f",&Ts);
	printf("Enter Ambient temperature(in celsius)  : ");
	scanf("%f",&Ta);
	printf("Enter windspeed at stack height(in m/s): ");
	scanf("%f",&uH);
	printf("Enter Delta(Ta)/Delta(Z)(in celsius/m) : ");
	scanf ("%f",&dtdz);

	F=g*pow(r,2)*Vs*(1-(Ta+273)/(Ts+273));
//	printf("F %f\n",F);
	if (F>=55) xf=120*pow(F,0.4);
	else xf=50*pow(F,0.625);
//	printf("xf %f\n",xf);
	s=g*(dtdz+0.01)/(Ta+273);
//	printf("s %f\n",s);

	printf("\nAtmosphere 1.Stable 2.Unstable??\n");
	scanf("%d",&cond1);
	ans1=plumerise(cond1);
	printf("Plume Rise is %f",ans1);

	printf("\nAtmosphere 1.Stable 2.Unstable??\n");
	scanf("%d",&cond2);
	ans2=plumerise(cond2);
	printf("Plume Rise is %f",ans2);

	printf("\nEnter the windspeed measured by Anemometer at 10m : ");
	scanf("%f",&uH3);
	printf("\nSee the condition and if true return value\n");
	printf("0. Clear summer day with sun higher than 60 degree above horizon\n");
	printf("1. Summer day,few broken clouds/clear dry day with sun 35-60 degree above horizon\n");
	printf("2. Fall afternoon/cloudy summer day/clear summer day with sun 15-35 degree above horizon\n");
	scanf("%d",&cond3);

	atmcl=findclass(cond3,uH3);
//	printf("class is %d\n",atmcl);
	if (atmcl<4) ans3=plumerise(2);
	else ans3=plumerise(1);
//	printf("plume rise %f",ans3);
	p=findexp(atmcl);
//	printf("p is %f\n",p);
	effh=hdash+ans3;
//	effh=100;

	ubar=uH3*pow((effh/10),p);
//	printf("\nubar%f",ubar);
//	printf("%f",findconc(2));

	for (i=1;i<=20;i++)
	{
//	printf("loop %d\n",i);
	y=findconc(x);
	printf("\nconc at %f km is %f",x,y);
	x=x+0.5;
	}

	return 0;
}
float plumerise(int cond)
{
	float dh;
	if (cond==1) dh=2.4*pow((F/(uH*s)),0.3333);
	else dh= (1.6*pow(F,0.3333)*pow(xf,0.6667))/uH;
	return dh;
}
int findclass(int cond,float uH2)
{
	int i;
	int atm[5][3]={0,0,1,0,1,2,1,1,2,2,2,3,2,3,3};
	if (uH2<2) i=0;
	else if (uH2>=2 & uH2<3) i=1;
	else if (uH2>=3 & uH2<5) i=2;
	else if (uH2>=5 & uH2<6) i=3;
	else i=4;
	return atm[i][cond];
}
float findexp(int atmclass)
{
	float exp[6]={0.15,0.15,0.20,0.25,0.4,0.6};
	return exp[atmclass];
}
void findvalues(int atmclass,float x)
{
	float values[6][8]={
		{213,440.8,1.941,9.27,459.7,2.094,-9.6},
		{156,106.6,1.149,3.3,108.2,1.098,2},
		{104,61,0.911,0,61,0.911,0},
		{68,33.2,0.725,-1.7,44.5,0.516,-13.0},
		{50.5,22.8,0.678,-1.3,55.4,0.305,-34},
		{34,14.35,0.740,-0.35,62.6,0.18,-48.6}
		};
	if (x<1)
	{
	a=values[atmclass][0];
	c=values[atmclass][1];
	d=values[atmclass][2];
	f=values[atmclass][3];}
	else
	{
	a=values[atmclass][0];
	c=values[atmclass][4];
	d=values[atmclass][5];
	f=values[atmclass][6];}
}
float findconc(float x)
{
	float conc;
	findvalues(atmcl,x);
//	printf("\nconstants %f %f %f %f",a,c,d,f);
	sigmay=a*pow(x,0.894);
	sigmaz=c*pow(x,d)+f;
//	printf("\nsigmay %f sigmaz %f\n",sigmay,sigmaz);
	conc= exp(-pow(effh,2)/(2*pow(sigmaz,2)))*(Q/(3.1416*ubar*sigmay*sigmaz));
	return conc;
}
