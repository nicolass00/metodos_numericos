clear all
%n=50;
%y=sort(rand(1,n))

n=10
dx=1/(n-1)
x=[4.4 4.5 4.8 5.5 5.7 5.9 6.3 6.9 7.5 7.8]
y=[13.1 9 10.4 13.8 12.7 9.9 13.8 16.4 17.6 18.3]

plot(x,y,'+')

A=[mean(x.^2) mean(x);mean(x) 1]

b=[mean(x.*y);mean(y)]
alfa=A\b

Y=alfa(1).*x+alfa(2)

plot(x,Y,x,y,'O')