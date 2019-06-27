package com.cg.pl;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Exercise1 {
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n,result=-1;
		ArrayList<Integer> a=new ArrayList<Integer>();
		System.out.println("Enter the Array Size");
		n=sc.nextInt();
		System.out.println("Enter the elements");
		for(int i=0;i<n;i++)
		{
			a.add(sc.nextInt());
		}
		result=getSecondSmallest(a);
		if (result==-1||result==0) 
			System.out.println("No Second Lowest Element");
		else
			System.out.println("Second Smallest Number is: "+result);
			
	}

	private static int getSecondSmallest(ArrayList<Integer> a) {
		// TODO Auto-generated method stub
		int min=0,k=0;
		Collections.sort(a);
		for(int i=0;i<a.size();i++)
		{
			if(k==a.get(i))
				{
				a.remove(i);
				i--;
				}
			else
				k=a.get(i);
		}
		if(a.size()>1)
		min=a.get(1);
		else
			min=0;
		return min;
	}

}
 