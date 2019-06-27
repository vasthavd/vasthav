package com.cg.pl;

public class Exercise2 {
	
	public static void main(String args[])
	{
		String [] array= {"Abc","Def","Xyz","Ijk","Mno"};
		int n=array.length;
		System.out.println("Length : "+n);
		int a=n/2;//if n=7,a=3
		for(int i=0;i<n;i++)
		{
			if(i<=a)
			array[i]=array[i].toUpperCase();
			else
			array[i]=array[i].toLowerCase();
		}
		for(int i=0;i<n;i++)
		{
		System.out.println(array[i]);
		}
	}
}
