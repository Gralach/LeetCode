func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
		return false
	}
    
	myMap_s := make(map[string]int)
	myMap_t := make(map[string]int)

	for index := range s {
		//s
		if _, exists := myMap_s[string(s[index])]; exists {
			myMap_s[string(s[index])] += 1
		} else {
			myMap_s[string(s[index])] = 1
		}

		//t
		if _, exists := myMap_t[string(t[index])]; exists {
			myMap_t[string(t[index])] += 1
		} else {
			myMap_t[string(t[index])] = 1
		}
	}

	for key, value1 := range myMap_s {
		value2, exists := myMap_t[key]
		if !exists || value1 != value2 {
			return false
		}
	}
	return true
}