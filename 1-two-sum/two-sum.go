func twoSum(nums []int, target int) []int {
    myMap := make(map[int]int)
    for index, value := range nums{
        if _, exists := myMap[target-value]; exists{
            return[]int{myMap[target-value], index}
        } else{
            myMap[value] = index
        }
    }
    return nil
}