package com.cg.eis.exception;

public class EmployeeException extends Exception{
	public EmployeeException() {
		// TODO Auto-generated constructor stub
	}
	public EmployeeException(String msg) {
		// TODO Auto-generated constructor stub
		super (msg);
		
	}
	@Override
	public String toString() {
		return "Exception - "+super.getMessage();
	}
}
