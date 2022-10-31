class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        if(s.length() != t.length())
            return false;
        for(int i = 0; i < s.length();i++){
            char c = s.charAt(i);
            if(map.get(c) == null){
                map.put(c, 1);
            } else {
                map.put(c, map.get(c)+1);
            }
        }
        System.out.println(map);
        for(int i = 0; i < s.length();i++){
            char c = t.charAt(i);
            if(map.get(c) == null || map.get(c) == 0){
                return false;
            } else {
                map.put(c, map.get(c)-1);
            }
        }
        return true;
    }
}