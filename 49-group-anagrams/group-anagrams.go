func groupAnagrams(strs []string) [][]string {
    myMap := make(map[string][]string)
	var groupedStrs [][]string

	for index := range strs {
		var arr [26]int
		for _, value := range strs[index] {
			arr[value-'a'] += 1
		}
		arrKey := fmt.Sprintf("%v", arr)
		myMap[arrKey] = append(myMap[arrKey], strs[index])
	}
	
	for _, group := range myMap {
		groupedStrs = append(groupedStrs, group)
	}

    return groupedStrs
}