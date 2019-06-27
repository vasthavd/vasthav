package com.cg.Lab5;

public interface Validator {
	
	String name ="[a-zA-Z]*+[']*[.]*[ ]*+[a-zA-Z]*+[ ]*+[a-zA-Z]*";
	
	String age="[0-9]*+[.]*+[0-9]*";
	
	String salary="[0-9]*+[.]*+[0-9]*";
	public static boolean validatedata(String data, String pattern)
	{
		return data.matches(pattern);
	}

}
