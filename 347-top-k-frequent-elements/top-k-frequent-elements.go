func topKFrequent(nums []int, k int) []int {
    myMap := make(map[int]int)

	buckets := make([][]int, len(nums)+1)
	var arr []int

	for _, values := range nums {
		if _, exists := myMap[values]; exists {
			myMap[values] += 1
		} else {
			myMap[values] = 1
		}
	}

	for key, values := range myMap {
		buckets[values] = append(buckets[values], key)
	}

	for i := len(buckets) - 1; i >= 0; i-- {
		for _, values := range buckets[i] {
			arr = append(arr, values)
            if len(arr) == k {
				return arr
			}
		}
	}

    return arr
}