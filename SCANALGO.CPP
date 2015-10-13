#include<conio.h>
#include<graphics.h>
#include<stdlib.h>
#include<math.h>
#include<dos.h>
#include<stdio.h>
class mouse                        //CLASS MOUSE
{
 private:
 union REGS in,out;
public:
 void initmouse()
{
 in.x.ax=0;
 int86(51,&in,&out);
}
void showmouse()
{
 in.x.ax=1;
 int86(51,&in,&out);
}
 void hidemouse()
{
 in.x.ax=2;
 int86(51,&in,&out);
}

int getmousepos(int &click,int &x,int&y)
{
 in.x.ax=3;
 int86(51,&in,&out);
 click=out.x.bx;
 x=out.x.cx;
 y=out.x.dx;
 return click;
}

void setxlimit(int x,int y)
{
 in.x.ax=7;
 in.x.cx=x;
 in.x.dx=y;
 int86(51,&in,&out);
}

void setylimit(int x,int y)
{
 in.x.ax=8;
 in.x.cx=x;
 in.x.dx=y;
 int86(51,&in,&out);
}


};

class polygon                              //CLASS POLYGON
{
 public:
 void bres(int x1,int y1,int x2,int y2);
 int sign(float);
 void scanfill(int[],int[],int,int);
};

void polygon::bres(int x1,int y1,int x2,int y2)        //Line drawing by bresenhams
{

int dx,dy,exchange,i,s1,s2,x,y,temp,g;
 dx=abs(x2-x1);
 dy=abs(y2-y1);

 s1=sign(x2-x1);
 s2=sign(y2-y1);

 x=x1;
 y=y1;
 if(dy>=dx)
 {
  temp=dy;
  dy=dx;
  dx=temp;
  exchange=1;
 }
 else
 exchange=0;

 g=2*dy-dx;
 for(i=1;i<dx;i++)
 {
  putpixel(x,y,WHITE);
  delay(10);

  while(g>=0)
  {
   if(exchange==1)
   x=x+s1;
   else
   y=y+s2;

   g=g-2*dx;
  }
  if(exchange==1)
  y=y+s2;
  else
  x=x+s1;
  g=g+2*dy;

}
}

int polygon::sign(float arg)
{
 if(arg<0)
 return -1;
 else if(arg==0)
 return 0;
 else
 return 1;
}

void polygon::scanfill(int xx[10],int yy[10],int col,int n)
{
 int i,k,interx[50],temp,y,ymax=0,ymin=480;
float m[50],dx,dy;
for(i=0;i<n;i++)
{
  if(yy[i]>=ymax)
  ymax=yy[i];
 if(yy[i]<=ymin)
 ymin=yy[i];

dx=xx[i+1]-xx[i];
dy=yy[i+1]-yy[i];

if(dx==0)
m[i]=0;

if(dy==0)
m[i]=1;

if(dx!=0 && dy!=0)
m[i]=(float)dx/dy;
}

int cnt;
setcolor(col);
for(y=ymax;y>=ymin;y--)
{
  cnt=0;
 for(i=0;i<n;i++)
 {
   if((yy[i]>y && yy[i+1]<=y) ||  (yy[i]<=y &&  yy[i+1]>y))
   {
	 interx[cnt]=(xx[i]+(m[i]*(y-yy[i])));
	 cnt++;
   }
}
for(k=0;k<cnt-1;k++)
 {
	for(i=0;i<cnt-1;i++)
	 {
	if(interx[i] > interx[i+1])
	 {
	   temp=interx[i];
	   interx[i]=interx[i+1];
	   interx[i+1]=temp;
	 }
	 }
}
for(i=0;i<cnt-1;i=i+2)
{
  line(interx[i],y,interx[i+1]+1,y);
  delay(10);
}
}
getch();

}

void main()
{
 int col,n,xx[10],yy[10],x,y,sy,sx,ch,gtx[5],gty[5],k=0;
mouse m;
polygon p;
int gdriver = DETECT, gmode, errorcode;

initgraph(&gdriver, &gmode, "");

errorcode = graphresult();

if (errorcode != grOk)
{
   printf("Graphics error: %s\n", grapherrormsg(errorcode));
   printf("Press any key to halt:");
   getch();
   exit(1);
}
m.initmouse();
m.showmouse();
 int click,i=0,x1,y1,x2,y2;
 do
 {
   delay(100);

   m.getmousepos(click,x,y);
   if(click==1)
	{
	  xx[k]=x;
	  yy[k]=y;
	  i++;
	  gtx[i]=x;
	  gty[i]=y;
	  k++;
	  if(i==2)
	  {
		x2=gtx[i];
		y2=gty[i];
		x1=gtx[1];
		y1=gty[1];
		p.bres(x1,y1,x2,y2);
		i=1;
		gtx[1]=x2;
		gty[1]=y2;
	  }
	}
 }while(!kbhit());
xx[k]=xx[0];
yy[k]=yy[0];
n=k;
p.scanfill(xx,yy,RED,n);

getch();
closegraph();
}

