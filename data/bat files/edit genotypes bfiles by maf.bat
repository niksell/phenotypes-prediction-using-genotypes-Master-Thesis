@ECHO OFF &SETLOCAL

cd "results of genotypes"
	
FOR /l %%A IN (1,1,22) DO (
	cd "chr%%A"
	C:\Users\ANTONIS\Desktop\plink\plink --assoc --bfile E:\chr%%A --1 --allow-no-sex  --maf 0.05  --pheno C:\Users\ANTONIS\Documents\GitHub\diplwmatikh\data\phenotype_edit.txt --out chr%%A

	cd ..
	
)

pause