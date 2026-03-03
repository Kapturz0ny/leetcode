class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()

        for k in range(len(nums)):
            if nums[k] > 0:
                break # all nums are positive

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = len(nums) - 1

            while i < j:
                ijk = nums[i] + nums[j] + nums[k]

                if ijk == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
                elif ijk > 0:
                    j -= 1
                else:
                    i += 1
            
        return triplets