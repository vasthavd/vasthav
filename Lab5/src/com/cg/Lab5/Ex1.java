package com.cg.Lab5;

import javax.swing.*;    
import java.awt.event.*;    
class Ex1 extends JFrame implements ActionListener{    
JRadioButton rb1,rb2,rb3;    
JButton b;    
Ex1(){      
rb1=new JRadioButton("Red");    
rb1.setBounds(100,50,100,30);      
rb2=new JRadioButton("Yellow");    
rb2.setBounds(100,100,100,30); 
rb3=new JRadioButton("Green");    
rb3.setBounds(100,150,100,30);
ButtonGroup bg=new ButtonGroup();    
bg.add(rb1);bg.add(rb2);bg.add(rb3);    
b=new JButton("click");    
b.setBounds(100,200,80,30);    
b.addActionListener(this);    
add(rb1);add(rb2);add(rb3);add(b);    
setSize(300,300);    
setLayout(null);    
setVisible(true);    
}    
public void actionPerformed(ActionEvent e){    
if(rb1.isSelected()){    
JOptionPane.showMessageDialog(this,"Stop");    
}    
if(rb2.isSelected()){    
JOptionPane.showMessageDialog(this,"Ready");    
}  
if(rb3.isSelected()){    
JOptionPane.showMessageDialog(this,"Go");    
} 
}    
public static void main(String args[]){    
new Ex1();    
}}   
