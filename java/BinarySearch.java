/**
 * 二分查找算法
 */
public class BinarySearch{
    public static void main(String[] args){
        double[] list = {1, 3, 6, 9, 12, 34};
        System.out.println(binarySearch(list, 34.0));
    }

    public static int binarySearch(double[] list, double item){
        int low = 0;
        int high = list.length - 1;
        while(low <= high){
            int mid = (int) (low + high) / 2;
            double guess = list[mid];
            if(guess < item){
                low = mid + 1;
            }else if(guess> item){
                high = mid - 1;
            }else{
                return mid;
            }
        }
        return -1;
    }
}