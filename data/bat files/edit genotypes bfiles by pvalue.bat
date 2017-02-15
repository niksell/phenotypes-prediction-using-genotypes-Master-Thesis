@ECHO OFF &SETLOCAL

cd "results of genotypes"
	
FOR /l %%A IN (1,1,14) DO (
	cd "chr%%A"
	C:\Users\ANTONIS\Desktop\plink\plink --bfile E:\genotypes\chr%%A --allow-no-sex --out chr%%A --1 --pheno E:\genotypes\phenotype_edit.txt --assoc fisher --pfilter 0.00001 
	
	cd ..
	
)

pause