/**
 * 选择排序算法
 */
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
public class SelectionSort{
    public static void main(String[] args){
        Double[] dl = {1., 7., 2., 65., 34., 24., 78., 55.};
        List<Double> list = Arrays.asList(dl);
        System.out.println(selectionSort(list, "Asce"));
    }

    public static int findMaxOrMin(List<Double> list, String sort){
        Double item = list.get(0);
        int item_index = 0;
        for (int i = 1; i < list.size(); i++) {
            if(sort.equals("Asce")){
                if(list.get(i) < item){
                    item = list.get(i);
                    item_index = i;
                }
            }else if(sort.equals("Desc")){
                if(list.get(i) > item){
                    item = list.get(i);
                    item_index = i;
                }
            }
        }
        return item_index;
    }
    public static List<Double> selectionSort(List<Double> list, String sort){
        // 因为List不能进行remove操作，所以这里用一个ArrayList进行操作
        ArrayList<Double> aList = new ArrayList<Double> ();
        for (Double var : list) {
            aList.add(var);
        }
        if(sort.equals("Desc") || sort.equals("Asce")){
            List<Double> newList = new ArrayList<Double>();
            int length = list.size();
            for(int i = 0; i < length; i++){
                int item_index = findMaxOrMin(aList, sort);
                newList.add(aList.remove(item_index));
            }
            return newList;
        }else{
            return null;
        }
    }
}