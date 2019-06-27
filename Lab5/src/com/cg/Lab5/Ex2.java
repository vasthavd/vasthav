package com.cg.Lab5;

import java.util.Scanner;

public class Ex2 {

	static int n1=0,n2=1,n3=0,i;   
	static int fibonacci (int count)
	{
	
	
	    
	 for(i=2;i<count;++i) 
	 {    
	  n3=n1+n2;    
	  n1=n2;    
	  n2=n3;    
	 } 
	 return n3;
	}
	
	public static int recFibonacci(int n)  {
	    if(n == 0)
	        return 0;
	    else if(n == 1)
	      return 1;
	   else
	      return fibonacci(n - 1);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		System.out.println("Enter number :- ");
		int n=sc.nextInt();
		
		int num=fibonacci(n);
		System.out.println("=========================================================");
		System.out.println("By Non Recursive method");
		System.out.println(n+"th value of the Fibonacci sequence is "+num);
		System.out.println("=========================================================");
		
		
		int num2=recFibonacci(n);
		System.out.println("=========================================================");
		System.out.println("By Recursive method");
		System.out.println(n+"th value of the Fibonacci sequence is "+num);
		
		System.out.println("=========================================================");
	}

}
