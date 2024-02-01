func twoSum(nums []int, target int) []int {
    for index, value := range nums{
        for index2 := index + 1; index2 < len(nums); index2++ {
            if value + nums[index2] == target {
                return []int{index, index2}
            }
        }
    }
    return nil
}