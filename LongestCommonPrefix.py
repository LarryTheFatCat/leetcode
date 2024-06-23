def longestCommonPrefix(strs: list[str]) -> str:
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix_list = []
    empty_string = ""

    if not strs:
        return empty_string

    for words in range(len(strs)):
        prefix_list.append(strs[words][:2])

    for prefixes in range(len(prefix_list) - 1):
        if prefix_list[prefixes] != prefix_list[prefixes + 1]:
            return empty_string

    return str(prefix_list[0])

def main():
    print(longestCommonPrefix(["ab", "a"]))

if __name__ == "__main__":
    main()
