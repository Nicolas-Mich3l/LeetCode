//You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

func mergeAlternately(word1 string, word2 string) string {
    var output []string
    var w1 = strings.Split(word1,"")
    var w2 = strings.Split(word2,"")
    length := 0 
    if len(w1) > len(w2){
        length = len(w1)
    } else {
        length = len(w2)
    }
    for i := 0; i < length; i++{
        if i < len(w1){
            output = append(output, w1[i])
        } 
        if i < len(w2) {
            output = append(output, w2[i])
        }
    }
    return strings.Join(output,"")
}
