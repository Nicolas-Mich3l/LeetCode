//There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0. You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

func largestAltitude(gain []int) int {
    var highest = 0 
    var current_height = 0 
    for i := 0; i < len(gain); i ++{
        current_height += gain[i]
        if current_height > highest {
            highest = current_height
        }
    }
    return highest 
}
