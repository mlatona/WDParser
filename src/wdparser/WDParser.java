/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package wdparser;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.StringWriter;
import javax.script.ScriptContext;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import javax.script.SimpleScriptContext;
import org.python.core.PyInteger;
import org.python.util.PythonInterpreter;
import org.python.core.*;

/**
 *
 * @author marco
 */
public class WDParser {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException, ScriptException {
       
       PythonInterpreter interpreter = new PythonInterpreter();
       interpreter.set("integer", new PyInteger(42));
      // interpreter.exec("for i in range(1,10):\nprint(i)");
      // PyInteger square = (PyInteger)interpreter.get("square");
      // System.out.println("square:" + square.asInt());
       interpreter.exec("from script import square");
       interpreter.exec("result = square(integer)");
       interpreter.exec("print(result)");
       PyInteger result = (PyInteger)interpreter.get("result");
       System.out.println(result);
       
        
        
        
        
        /*StringWriter writer = new StringWriter(); //ouput will be stored here

            ScriptEngineManager manager = new ScriptEngineManager();
            ScriptContext context = new SimpleScriptContext();

            context.setWriter(writer); //configures output redirection
            ScriptEngine engine = manager.getEngineByName("python");
            FileReader file = new FileReader("script.py");
           
         //   System.out.println(file.canRead());
         //   System.out.println(file.getName());
            
            engine.eval(file, context);
            System.out.println(writer.toString()); 
        */
    }
                
    
}
