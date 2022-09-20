function[y]=f_prima(x)
y=[];
for i=1:1:length(x)
    yo=6*x(i)-exp(x(i));
    y=[y yo];
end