function[y]=f(x)
y=[];
for i=1:1:length(x)
    yo=3*x(i)^2-exp(x(i));
    y=[y yo];
end
