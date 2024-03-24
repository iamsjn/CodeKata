def subsequences(s):
    sub_seqs = []
    for i in range(len(s)):
        j = i
        k = j
        sub_seq = s[i]
        while k < len(s):
            if sub_seq not in sub_seqs:
                sub_seqs.append(sub_seq)
            j = j + 1
            if j == len(s):
                k = k + 2
                j = i + 2
                if j < len(s):
                    sub_seq = s[i] + s[j]
            else:
                sub_seq = sub_seq + s[j]
    print(sub_seqs)


if __name__ == "__main__":
    subsequences("apple")
