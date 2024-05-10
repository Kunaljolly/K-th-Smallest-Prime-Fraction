class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        t = []
        s = []
        for x in range(len(arr)-1):
            for y in range(len(arr)):
                if x == y : continue
                t.append(str(arr[x])+"/"+str(arr[y]))
                s.append(arr[x]/arr[y])
        s2 = sorted(s)
        k = t[s.index(s2[k-1])]
        k2 = [int(x) for x in k.split("/")]
        return k2

