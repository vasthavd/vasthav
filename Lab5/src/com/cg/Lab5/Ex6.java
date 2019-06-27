package com.cg.Lab5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import com.cg.eis.exception.*;


public class Ex6 {


	public static void main(String[] args) throws UserException, IOException{
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Double salary=0.0;
		System.out.println("Enter Employee Salary");
		 while(true)
		  {
			 
			 String input=br.readLine();
			  boolean ch1=Validator.validatedata(input, Validator.salary);
			  if(ch1==true)
			  {
				  try {
					   salary= Double.parseDouble(input);
					   break;
				  }
				  catch(NumberFormatException e)
			  
			  {
				 System.out.println("Salary must be Numeric. Re Enter"); 
			  }
		  }
			  else
			  {
				  System.out.println("Re Enter Salary");
			  }
		  
		  }
		 try {
			 if(salary<3000)
			 {
				 throw new EmployeeException();
			 }
		 }
		 catch(EmployeeException e)
		 {
			 System.err.println("Exception :- Salary should be greater than 3000");
		 }
		 
}
}