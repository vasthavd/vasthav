package com.cg.eis.exception;

public class UserException extends Exception {
	//Exception raises when employees does'nt fall in any category and salary range is matching with designation...	
	public UserException() {
		// TODO Auto-generated constructor stub
	}
	public UserException(String msg) {
		// TODO Auto-generated constructor stub
		super (msg);
		
	}
	@Override
	public String toString() {
		return "Exception - "+super.getMessage();
	}
}
