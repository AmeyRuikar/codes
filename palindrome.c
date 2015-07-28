#include<stdio.h>
#include<string.h>

int main()
{

	char	str[500];
	
	scanf("%s", str);
	
	
	int	len;
	int	i, j;
	
	len = strlen(str);
	
	
	i = len / 2;
	
	if(len % 2 ==0)//even length
	{
	
		
		for(j = 0 ; j < i; j++){
		
		
			if( str[i- j - 1] == str[i+j]){
			
			}
			else
			{
				printf("not palindrome");
				break;
			}
		
		
		}
	
	
	
	
	}
	else	//odd length
	{
	
		
		
		for(j = 1; j <= i; j++)
		{
		
			if(str[i - j] == str[i + j])
			{
			}
			else
			{
				printf("not palindrome");
				break;
			}
			
		
		}
			
			
			
	
	
	
	}
	
	


	return	0;
}
