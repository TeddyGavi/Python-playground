class Solution:
    def valid_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            map = {}
            for i in s:
                if i in map:
                    map[i] += 1
                else:
                    map[i] = 1

            for i in t:
                if i in map:
                    if map[i] == 0:
                        return False
                    else:
                        map[i] -= 1
                else:
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()

    result = solution.valid_anagram("bob", "bob")
    print(result)
