public class Dictionary_genarator {
    public String[] uppper_case_generator(){
        int counter =0;
        String[] upper_case_table = new String[(int)(0x5A-0x40)];

        for (int i = 0x41; i <= 0x5A  ; i++){
            upper_case_table[counter] = Character.toString( (char) i);
            counter += 1;
        }

        return upper_case_table;
    }
    public String[] lower_case_generator(){
        int counter =0;
        String[] lower_case_table = new String[(int)(0x7A-0x60)];

        for (int i = 0x61; i <= 0x7A  ; i++){
            lower_case_table[counter] = Character.toString( (char) i);
            counter += 1;
        }

        return lower_case_table;
    }
    public String[] chinese_character_generator(){
        int counter = 0;
        String[] chinese_character_table = new String[(int)(0x9ff0-0x4dff)];
        for (int i = 0x4e00; i <= 0x9ff0  ; i++){
            chinese_character_table[counter] = Character.toString( (char) i);
            counter += 1;
        }
        return chinese_character_table;
    }

    public static void main(String[] args) {

        Dictionary_genarator Dict = new Dictionary_genarator();

        String[] upper_case = Dict.uppper_case_generator();
        String[] lower_case = Dict.lower_case_generator();
        String[] chinese_character = Dict.chinese_character_generator();

    }
}
