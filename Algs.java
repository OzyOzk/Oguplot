public class Main
{
    public static void main(String[] args)
    {
        printFB(3, 5);
        printFib(0);
    }

    public static void fizzbuzz(int fizz, int buzz)
    {
        int fz = 0;
        int bz = 0;

        for(int i = 1; i <= 100; i++)
        {
            fz++;
            bz++;

            if(fz == fizz)
            {
                System.out.print("fizz");
                fz=0;
            }
            if(bz == buzz)
            {
                System.out.print("buzz");
                bz=0;
            }

            if(fz !=0 && bz != 0)
            {
                System.out.print(i);
            }

            System.out.print("\n");
        }
    }

    public static void printFB(int fizz, int buzz)
    {
        String fizzbuzz = "";
        for(int i = 1; i <=100; i++)
        {
            if(i%fizz == 0) fizzbuzz+="fizz";
            if(i%buzz == 0) fizzbuzz+="buzz";

            if(fizzbuzz.isEmpty()) System.out.print(i);
            else
            {
                System.out.print(fizzbuzz);
                fizzbuzz = "";
            }
            System.out.println();

        }
    }

    public static void printFib(int n)
    {
        int t2 = 0;
        int t1 = 1;
        int tn = 0;

        for(int i =0; i < n; i++)
        {
            tn = t1+t2;
            System.out.println(tn);
            t2 = t1;
            t1 = tn;
        }
    }

}
