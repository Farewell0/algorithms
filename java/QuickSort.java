/**
 * 快速排序算法  分而治之的策略
 */
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class QuickSort{
    public static void main(String[] args){
        Integer[] arr = {2, 56, 1, 34, 12, 76, 45};
        List<Integer> list = Arrays.asList(arr);
        System.out.println(quickSort(list));
    }

    public static List<Integer> quickSort(List<Integer> list){
        if(list.size() < 2){
            return list;
        }else{
            int pivot = list.get(0);
            List<Integer> less = new ArrayList<Integer> ();
            List<Integer> greater = new ArrayList<Integer> ();
            for(int i = 1; i < list.size(); i++){
                if(list.get(i) <= pivot)
                    less.add(list.get(i));
                else
                    greater.add(list.get(i));
            }
            less = quickSort(less);
            less.add(pivot);
            less.addAll(quickSort(greater));
            return less;
        }
    }
}