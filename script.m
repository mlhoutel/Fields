% Param�tres g�om�triques du capteur :
R=0;
L=0;
U=0;
espilon = 1;

% Param�tres de la grille de points centr�e autour du capteur :
Xmin=-1;
Xmax=1;
Ymin=-1;
Ymax=1;
dx=0.05;
dy=0.05;

% Calcul du courant I et de la quantit� surfacique de charge Sigma:
I = 0; % A compl�ter
Sigma = 0; % A compl�ter

% Cr�ation de la grille de points :
[X,Y]=meshgrid(Xmin:dx:Xmax,Ymin:dy:Ymax);

% Evaluation en chaque point de la grille de la valeur du potentiel
% �lectrique :
[n,m]=size(X);
V=zeros(n,m);

for i=1:1:n
	for j=1:1:m
        R1 = 0; % A compl�ter 
        R2 = 0; % A compl�ter
        
        if (R1 < R)
            V(i,j) = 0; % A compl�ter 
        elseif (R2 < R)
            V(i,j) = 0; % A compl�ter     
        else
            V(i,j) = 0; % A compl�ter 
        end
        
	end
end

% Evaluation en chaque point de la grille du champ �lectrique :
[Ex,Ey]=gradient(V,dx,dy);

% Plot :
figure;
contour(X,Y,V);
hold on;
streamslice(X,Y,Ex,Ey); # voir quiver
axis equal
xlabel('x (m)');
ylabel('y (m)');
hold off