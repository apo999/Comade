%plot for test
y=loadsig('test.tr0');
char=lssig(y)
for index=1:1:length(char(:,1))
	figure(index)
	plotsig(y,char(index,:));
end
