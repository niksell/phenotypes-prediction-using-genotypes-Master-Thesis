@ECHO OFF &SETLOCAL


	
FOR /l %%A IN (1,1,22) DO (
	
	C:\Users\ANTONIS\Desktop\plink\plink --recode lgen --out "chr%%A" --keep-fam patient.txt --bfile E:\genotypes\chr%%A --1 --allow-no-sex --extract "chr%%AsnpList.txt"
	
	
)

pause