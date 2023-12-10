% function [DFB_new,DFC_new,DFD_new,DFE_new]=rtc_fit(DFB,DFC,DFD,DFE,Tr,sumerror)

% DFB=-4096;
% DFC=-75925;
% DFD=20884;
% DFE=3000;
% % 
% Tr=[26
% 37.3
% 52.8
% 67.5
% 82.6];
% sumerror=[0.15552
% 0.4536
% 0.88992
% 1.26144
% 1.53792];



% DFB=-10061;
% DFC=-75925;
% DFD=20884;
% DFE=3000;
% Tr=[-38.9
% -10.6
% 26.6
% 59.8
% 85.7];
% sumerror=[0.50803
% 0.36028
% -0.00604
% -0.47088
% -0.99792];



% DFB=-10061;
% DFC=-75925;
% DFD=20884;
% DFE=3000;
% Tr=[-38.9
% -10.6
% 26.6
% 59.8
% 85.7];
% sumerror=[0.40781
% 0.30931
% -0.03283
% -0.46483
% -0.95645];


DFB=-9000;
DFC=-75000;
DFD=20884;
DFE=3000;

Tr=[-25;0;25;60];
sumerror=[2;0;0;0];


% 1.Tr -> t
Toff=0;
DFA=0;

TMPDAT = (12.9852 - Tr)./0.00278;
t = (TMPDAT - Toff)./2^16;

% 2.DFi
DFi = DFB*t + DFC*t.^2 + DFD*t.^3 + DFE*t.^4;

% 3.error -> delta DFi
% delta_ppm = (sumerror - 0.000879169)./0.086391696;

delta_ppm = (sumerror)./(24*60*60*1e-6);
delta_DFi = delta_ppm./0.015;

% 4.DFi_new
DFi_new = DFi + delta_DFi;


% 5.DFi_new - constant
DFi_coe = [DFB , DFC , DFD , DFE];
DFi_item = zeros(length(DFi),4);

for i=1:4
    DFi_item(:,i) = DFi_coe(i)*t.^(i);
end

num=length(Tr);
if num==5
    DFi_new = DFi_new;
elseif num==4
    DFi_new = DFi_new - DFi_item(:,4);
elseif num==3
    DFi_new = DFi_new - DFi_item(:,4) - DFi_item(:,3);
elseif num==2
    DFi_new = DFi_new - DFi_item(:,4) - DFi_item(:,3) - DFi_item(:,2);
else
    DFi_new = 0;
end

% 6.fit
p=polyfit(t,DFi_new,length(t)-1);

if num==5
    DFi_coe = p(4:-1:1);
elseif num==4
    DFi_coe(1:3) = p(3:-1:1);
elseif num==3
    DFi_coe(1:2) = p(2:-1:1);
elseif num==2
    DFi_coe(1) = p(1);
else
    DFi_coe = DFi_coe;
end

DFi_coe=round(DFi_coe);

DFB_new=DFi_coe(1);
DFC_new=DFi_coe(2);
DFD_new=DFi_coe(3);
DFE_new=DFi_coe(4);
