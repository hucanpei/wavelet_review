clear;clc;
Fig=double(zeros(1600,1600));
x=1:1600;
y=1:1600;
for i=1:1600
    for j=1:1600
        Fig(i,j)=((1600-x(i))+y(j))*255/3200;
    end
end
%Fig=uint8(Fig);
%imshow(Fig);
Fig_cells=mat2cell(Fig,[400 400 400 400],[100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100]);
Fig_cells_means=cellfun(@mean,cellfun(@mean,Fig_cells,'UniformOutput',false));

col1=uint8(Fig_cells_means(1,:));
cells_col2=mat2cell(Fig_cells_means(2,:),1,[2 2 2 2 2 2 2 2]);
col2=uint8(cellfun(@mean,cellfun(@mean,cells_col2,'UniformOutput',false)));
cells_col3=mat2cell(Fig_cells_means(3,:),1,[4 4 4 4]);
col3=uint8(cellfun(@mean,cellfun(@mean,cells_col3,'UniformOutput',false)));
cells_col4=mat2cell(Fig_cells_means(4,:),1,[8 8]);
col4=uint8(cellfun(@mean,cellfun(@mean,cells_col4,'UniformOutput',false)));

col1=dec2hex(col1);
col2=dec2hex(col2);
col3=dec2hex(col3);
col4=dec2hex(col4);
