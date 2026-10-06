/*import java.util.*;
public class ne {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int age=sc.nextInt();

        if(age>18){
            System.out.println("Adult");
        } else{
            System.out.println("Not adult");
        }
    }
    
    
}*/


/*import java.util.*;
public class ne{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        float marks=sc.nextInt();

        if(marks>=75){
            System.out.println("A Grade");

        } else if(marks>=60) {
            System.out.println("B Grade");
            
        } else if(marks==0){
            System.out.println("Fail");
        }
    }
}*/

/*import /*java.util.*;
public class ne{
    public static void main(String[] args) {
         System.out.println("Choose any 1 button\n1 for Call of duty\n2 for Free fire\n3 for BGMI ");3

        Scanner sc=new Scanner(System.in);
        int button=sc.nextInt();
        

        switch(button){
            case 1:
                System.out.println("Call Of Duty");
                break;
            case 2:
                System.out.println("Free Fire");
                break;
            case 3:
                System.out.println("BGMI");
                break;
            default:
                System.out.println("Wrong selection");    

        }
        
    }
}**/

/*import java.util.*;
public class ne{
    public static void main(String[] args) {
        System.out.println("Enter any number");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sum=0;

        for(int i=0;i<=n;i--){
            sum=sum-i;

        }
        System.out.println("sum of n number is:\n"+sum);
    }
}*/

/*import java.util.*;
public class ne{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=4;
        int m=5;

        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(i==1||j==1||i==n||j==m){
                    System.out.print("*");
                } else{
                    System.out.print(" ");
                }
            }
            System.out.println(" ");
           
        }
        System.out.println();

       
    }
    
}*/

/*import java.util.*;
public class ne{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();

        int max=a;
        if(b>max){
            max=b;
        }
        if(c>max){
            max=c;
        }
        System.out.println( "greater is :"+max);

        

    }
}*/

//fibnahci series 

/*import java.util.*;
public class ne{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a=0;
        int b=1;

        int count=2;

        while(count<=n){
            int temp=b;
            b=b+a;
            a=temp;
            count++;

        }
        System.out.println(b);
    }

}*/

//checking repetion of number;
/*import java.util.*;
public class ne{
    public static void main(String[] args) {
        int n=754944;
        int count=0;
         while(n>0){
            int rem=n%10;
            if(rem==4){
                count++;
            }
            n=n/10;
         }
         System.out.println(count);
    }
}*/

import java.util.*;
public class ne{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter your name: ");
        String name=sc.nextLine();

        System.out.println("Enter your age: ");
        int age=sc.nextInt();
        sc.nextLine();

        System.out.println("Enter your college name: ");
        String colege_name=sc.nextLine();

        System.out.println("Enter target placement year: ");
        int target_Placement_Year=sc.nextInt();

        int currentYear=2026;
        int remainingYear=target_Placement_Year-currentYear;

        System.out.println("===Student Profile===");
        System.out.println("Name is: "+name);
        System.out.println("Age is: "+age);
        System.out.println("College name: "+colege_name);
        System.out.println("Placement target year: "+target_Placement_Year);
        System.out.println("Remaining year is: "+remainingYear);
    }
}
