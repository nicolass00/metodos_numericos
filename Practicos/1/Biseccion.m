Xmax=input('Ingrese el intervalo superior: ');
Xmin=input('Ingrese el intervalo inferior: ');
t=input('Ingrese un valor de tolerancia: ');
e=10*t;
E=[];
if f(Xmin)*f(Xmax)<0
    while e>t
        Xo=(Xmax+Xmin)/2;
        if f(Xmin)*f(Xo)<0
            Xmax=Xo;
            e=abs(Xmin-Xo);
        else
            if f(Xmin)*f(Xo)>0
                Xmin=Xo;
                e=abs(Xmax-Xo);
            else
                e=0;
            end
        end
        E=[E e];
    end
    x=linspace(Xmin,Xmax,1000);
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
else
	disp('El intervalo no contiene una unica raiz, intente de nuevo')
end
