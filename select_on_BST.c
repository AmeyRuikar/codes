#include<stdio.h>
#include<stdlib.h>

#define RIGHT 1
#define	LEFT  2


typedef struct node{

	int	data;
	struct node *	right;
	struct node *	left;

}node;


int last = 0;

void	insert(struct node * ptr, int data)
{

	struct	node *	temp;
	
		
		if( ptr->data > data)//go left
		{
		
			if(ptr->left == NULL)
			{
			
				temp = (node *) malloc(sizeof(node));
				
				ptr->left = temp;
				
				temp->data = data;
				
				temp->right = temp->left = NULL;
			
			}
			else
			{
			
				insert(ptr->left, data);
			
			}
		
		
		
		}
		else{//go right
		
			if(ptr->right == NULL)
			{
			
				temp = (node *) malloc(sizeof(node));
				
				ptr->right = temp;
				
				temp->data = data;
				
				temp->right = temp->left = NULL;
			
			}
			else
			{
			
				insert(ptr->right, data);
			
			}
		
		}	
		
		
	
	return;	

}

void	inorder(struct node * ptr)
{

	if(ptr == NULL)
		return;
		
	inorder(ptr->left);
	
	printf("%d", ptr->data);
	printf("(%d) ", (calculate_nodes(ptr->left) + calculate_nodes(ptr->right)));
	
	
	inorder(ptr->right);

}

int select_2(struct node * ptr, int x){

	
	int	nodes_left;
	int	nodes_right;
	
	nodes_left = calculate_nodes(ptr->left);	
	printf("\nnodes_left = %d\n", nodes_left);
	
	/*
	if( last==RIGHT )
	{
		printf("\nlast right");
		if(x==1)
			return ptr->data;
	}
	*/
	if( x == (nodes_left + 1))
		return ptr->data;
	
	if( nodes_left < x){
		printf("\nmoved right");
		last = RIGHT;
		return select_2(ptr->right, x - nodes_left - 1);
		
	
	}else{
	
		if( x <= nodes_left){
		
			printf("\nmoved left");
			last = LEFT;
			return select_2(ptr->left, x );
	
		}
	
	}
}

int calculate_nodes(struct node * ptr){


	if(ptr==NULL)
		return 0;

	if(ptr->right==NULL && ptr->left==NULL){
		return 1;
	}
	
	return (1 + calculate_nodes(ptr->left) + calculate_nodes(ptr->right));

}

int	main(){


	struct node * head;
	int	x;
	int	choice, n;
	int	nodes;
	
	
	printf("enter root node's data:");
	scanf("%d", &x);
	
	
	head = (node *) malloc(sizeof(node));

	head->data = x;
	head->right = head->left = NULL;
	
	
	do{
	
		printf("\n1 - insert node");
		printf("\n2 - SELECT the nth smallest node");
		printf("\n3 - exit::");
		
		scanf("%d", &choice);
		
		
		switch(choice){
		
			case 1:
				
				printf("enter data:");
				scanf("%d", &x);
				
				insert(head ,x);
			
			
				break;
			case 2:
			
				printf("enter n for nth smallest number");
				scanf("%d", &x);
				
				printf("\n\n%dth smallest number:%d\n",x,select_2(head, x));
		
				break;
		
		
		}
	
	
	
	}while(choice != 3);

	
	inorder(head);

	return	0;
}
