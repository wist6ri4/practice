import java.io.*;

public class HeapTest2 {
    public static void main(String[] args) throws InterruptedException {
        sayHello();

        StringBuffer oldStr = new StringBuffer(5000000);
        int i = 0;
        while(true) {
            StringBuffer newStr = new StringBuffer(100000);
            Thread.sleep(100);
        }
    }

    public static void sayHello() {
        System.out.print("Hello");
        StringBuffer tempStr = new StringBuffer(30000000);
    }
}
