func productExceptSelf(nums []int) []int {
    //length := len(nums)
    res:= make([]int, len(nums))
    prefix := 1
    for i := range nums{
        res[i] = prefix
        prefix *= nums[i]
    }
    postfix := 1
    for i := len(nums) - 1; i > -1; i--{
        res[i] *= postfix
        postfix *= nums[i]
    }
    return res
}