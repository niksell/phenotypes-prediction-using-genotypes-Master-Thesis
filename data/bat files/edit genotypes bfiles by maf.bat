@ECHO OFF &SETLOCAL

	
FOR /l %%A IN (1,1,22) DO (
	
	C:\Users\ANTONIS\Desktop\plink\plink --assoc --bfile F:\chr%%A --1 --allow-no-sex  --maf 0.05  --pheno case_control_unrelated.txt --out chr%%A

	
	
)

pause