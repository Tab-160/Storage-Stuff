
/**
 * Write a description of class class1 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.io.*;
public class class1{
    

    public class1(){}

    //InterruptedException
    public void sampleMethod(){
        try{
            try{
                Process process = Runtime.getRuntime().exec("cmd /c start chessboard.py");
                process.waitFor();
                int exitCode = process.exitValue();
                System.out.println(exitCode);
            }
            catch (InterruptedException e){
                System.out.println("Fail2 " + e.getMessage());
            }
        }
        catch (IOException e){
            System.out.println("Failed" + e.getMessage());
        }
    }
}
