class Solution:
    def minOperations(self, logs: List[str]) -> int:

        dir_ = []
        for i in logs:

            if i[0]!= ".":
                dir_.append(i[:-1])

            if i[0] == "." and i[1] == ".":
                if dir_ != []:
                    dir_ = dir_[:-1]
            
        print(dir_)

        return len(dir_)