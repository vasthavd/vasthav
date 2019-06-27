package com.cg.pl;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Exercise3 {

	public static void main(String args[]) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			System.out.println("enter number of elements");
			int[] array = new int[Integer.parseInt(br.readLine())];
			
			for(int i=0;i<array.length;i++) {
				array[i] = Integer.parseInt(br.readLine());
			}
			array = getSorted (array);
			
			Arrays.sort(array);
			
			System.out.println("after sorting");
			for(int i : array) {
				System.out.println(i);
			}
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
	
	public static int[] getSorted (int[] array) {
		
		for(int i=0;i<array.length;i++) {
			StringBuilder sb = new StringBuilder(String.valueOf(array[i])); 
			String element = sb.reverse().toString();
			array[i] = Integer.parseInt(element);
		}
		
		return array;
	}
}


