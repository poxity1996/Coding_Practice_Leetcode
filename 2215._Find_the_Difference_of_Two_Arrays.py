class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        def get_unique(source_set,compare_set):
            unique = []
            for i in source_set:
                if i not in compare_set:
                    unique.append(i)
            return unique

        s1,s2 = set(nums1),set(nums2)

        res1 = get_unique(s1,s2)
        res2 = get_unique(s2,s1)

        return [res1,res2]