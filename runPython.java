
/**
 * This is a class that runs a python program.
 *
 * @author Rab Greenup
 * @version 1.0.0
 */
import java.io.*;
public class class1{
    

    public class1(){}

    //InterruptedException
    public void sampleMethod(){
        try{
            try{
                Process process = Runtime.getRuntime().exec("cmd /c start programNameGoesHere.py");
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
