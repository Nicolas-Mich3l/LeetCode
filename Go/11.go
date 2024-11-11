//You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store. Notice that you may not slant the container.



func maxArea(height []int) int {
    // Area = width * height
    // height = height of the lower of the two lines forming walls
    // width = difference of indicies 
    l := 0 
    r := len(height)-1
    current := 0 
    for l < r {
        volume := min(height[l],height[r]) * (r-l)
        if volume > current {
            current = volume
        }
        if max(height[l],height[r]) == height[l]{
            r--
        } else {
            l ++
        }
    }
    return current   
}
