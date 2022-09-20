Xo=input('Ingrese un valor de prueba: ');
t=input('Ingrese un valor de tolerancia: ');
X1=Xo-f(Xo)/f_prima(Xo);
e=10*t;
E=[];
while e>t
	Xo=X1;
	X1=Xo-f(Xo)/f_prima(Xo);
    e=abs(X1-Xo);
    E=[E e];
end
if isnan(Xo)==1
    disp('El valor de prueba ingresado produce una divergencia, intente de nuevo');
else
    x=linspace(Xo-0.5, Xo+0.5, 1000);
    y=f(x);
    I=1:1:length(E);
    subplot(2,1,1);
    plot(x,y);
    grid on
    xlabel('x');
    ylabel('f(x)')
    subplot(2,1,2);
    plot(I,E);
    grid on
    xlabel('Iteracion');
    ylabel('Error')
    fprintf('La raiz de la funcion es: %8.16f\n', Xo);
end