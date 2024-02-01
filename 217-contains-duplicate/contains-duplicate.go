func containsDuplicate(nums []int) bool {
    
    myMap := make(map[int]bool)

    for _, value := range nums{
        if _, exists := myMap[value]; exists {
            return true
        }
        myMap[value] = true
    }
    return false
}