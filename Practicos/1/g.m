function[y]=g(x)
y=[];
for i=1:1:length(x)
    yo=exp(x(i))/(3*x(i));
    y=[y yo];
end
